# WebAssembly: Das neue Docker und noch mehr?

> If WASM+WASI existed in 2008, we wouldn’t have needed to created Docker. That’s how important it is. Webassembly on the server is the future of computing. A standardized system interface was the missing link. Let’s hope WASI is up to the task!

— [Tweet](https://twitter.com/solomonstre/status/1111004913222324225 "Tweet"), Solomon Hykes (Erfinder von Docker), 2019

Dieser Tweet über *WebAssembly (WASM)* des Docker-Erfinders gibt einen Hinweis auf die mögliche Innovationskraft dieser Technologie. Der vorliegende Artikel vermittelt zunächst die wichtigsten technischen Grundlagen von WebAssembly, welche zum weiteren Verständnis notwendig sind. Anschließend wird der *WASI-Standard* näher beleuchtet, welcher die Brücke zur Containervirtualisierung schlägt. Schließlich betrachten wir mit *Krustlet (Kubernetes)* und *wasmCloud* zwei existierende Cloud-Technologien, die zentral auf WebAssembly basieren.

## 1. WebAssembly (WASM)

### 1.1. WebAssembly als Number Cruncher für JavaScript

> Any application that can be written in JavaScript, will eventually be written in JavaScript.

— [Atwood's Law](https://en.wikipedia.org/wiki/Jeff_Atwood "Atwood's Law"), Jeff Atwood (Mitgründer von StackOverflow)