# WebAssembly: Das neue Docker und noch mehr?

> If WASM+WASI existed in 2008, we wouldn’t have needed to created Docker. That’s how important it is. Webassembly on the server is the future of computing. A standardized system interface was the missing link. Let’s hope WASI is up to the task!

— [Tweet](https://twitter.com/solomonstre/status/1111004913222324225 "Tweet"), Solomon Hykes (Erfinder von Docker), 2019

Dieser Tweet über WebAssembly (WASM) des Docker-Erfinders gibt einen Hinweis auf die mögliche Innovationskraft dieser Technologie. Der vorliegende Artikel vermittelt zunächst die wichtigsten technischen Grundlagen von WebAssembly, welche zum weiteren Verständnis notwendig sind. Anschließend wird der WASI-Standard näher beleuchtet, welcher die Brücke zur Containervirtualisierung schlägt. Schließlich betrachten wir mit Krustlet (Kubernetes) und wasmCloud zwei existierende Cloud-Technologien, die zentral auf WebAssembly basieren.

## 1. WebAssembly (WASM)

### 1.1. WebAssembly als Number Cruncher für JavaScript

> Any application that can be written in JavaScript, will eventually be written in JavaScript.

— [Atwood's Law](https://en.wikipedia.org/wiki/Jeff_Atwood "Atwood's Law"), Jeff Atwood (Mitgründer von StackOverflow)

Die gestiegene Popularität und weite Verbreitung von JavaScript (JS) innerhalb der vergangenen Jahre drückt sich pointiert im *Atwood'schen Gesetz* aus. Dieses besagt: Falls es möglich ist, dass eine Anwendung in JavaScript implementiert werden kann, wird das auch irgendwann so geschehen.

[JavaScript Engines](https://en.wikipedia.org/wiki/JavaScript_engine "JavaScript Engines") wurden im Zuge des Erfolgs der Sprache und des Wettbewerbs zwischen den Browsern beträchtlich [performanter](https://v8.dev/blog/10-years#performance-ups-and-downs "performanter"). Da JavaScript aber letztlich eine Sprache mit dynamischer Typisierung ist, unterliegt die Optimierung der Performance gewissen Grenzen. Daher ergibt es wenig Sinn, rechenintensive Anwendungen damit zu realisieren.

Für rechenintensive Anwendungen soll [WebAssembly (WASM)](https://webassembly.org/ "WebAssembly (WASM)") Abhilfe schaffen. Bei der Technologie handelt es sich um ein Bytecode-Format für eine entsprechende virtuelle Maschine (VM). WASM wurde so konzipiert, dass performante Sprachen wie z.B. [C/C++, Rust, AssemblyScript oder TinyGo](https://github.com/appcypher/awesome-wasm-langs "C/C++, Rust oder TinyGo") [19] für diese VM kompiliert werden können. Am Ende erhält man eine wasm-Datei, die den Bytecode enthält und in JavaScript dann über die [WebAssembly API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly "WebAssembly API") des Browsers (bzw. der JS Engine) geladen und ausgeführt werden kann. Das Minimalbeispiel im folgenden Kapitel soll den Workflow verdeutlichen.

![WebAssembly Compiler Target, Lin Clark](figures/external/lin-clark-compiler-target.png)
— *Abb: Verschiedenste Sprachen können zu WebAssembly Bytecode kompiliert werden. Zeichnung von [Lin Clark](https://hacks.mozilla.org/2017/02/creating-and-working-with-webassembly-modules/) [18]*

### 1.2. Workflow / Beispielprojekt

Wir gehen von einem akademischen Beispiel aus, welches in der Quelltextdatei `program.c` implementiert wurde:

``` c
// program.c

void external_number_printer(int number);

int add(int a, int b) {
    int result = a + b;
    external_number_printer(result);
    return result;
}
```

Die Funktion `add()` gibt das Ergebnis einer Addition zurück. Zusätzlich wird die Funktion `external_number_printer()` mit dem Ergebnis aufgerufen. Diese wird erst zur Laufzeit durch JavaScript bereitgestellt und daher in C nur deklariert.

Übersetzt wird der Quelltext mit einem Compiler, welcher WASM als Zielarchitektur unterstützt. In diesem Beispiel mit [Clang (LLVM Projekt)](https://clang.llvm.org/ "Clang (LLVM)") [1]:

``` sh
clang --target=wasm32 --no-standard-libraries -Wl,--export-all -Wl,--no-entry -Wl,--allow-undefined -o program.wasm program.c
```

Ergebnis ist die Bytecode-Datei `program.wasm`. Diese kann in JavaScript geladen werden, um die Funktion `add()` auszuführen. Die Funktion `external_number_printer()` wird dabei per `importObject` bereitgestellt.

``` javascript
// script.js

function js_number_printer(number) {
    console.log('JS Number Printer: ' + number);
}

async function main() {
    const source = fetch('program.wasm');
    const importObject = { env: { external_number_printer: js_number_printer } };
    const { instance } = await WebAssembly.instantiateStreaming(source, importObject);

    const result = instance.exports.add(40, 2); // call webassembly function
    console.log('Result: ' + result);
}

main();
```