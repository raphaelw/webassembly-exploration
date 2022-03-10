// script.js
function js_number_printer(number) {
    console.log('JS Number Printer: ' + number);
}

async function main() {
    const source = fetch('program.wasm');
    const importObject = { env: { external_number_printer: js_number_printer } };
    const { instance } = await WebAssembly.instantiateStreaming(source, importObject);

    const result = instance.exports.add(40, 2);
    console.log('Result: ' + result);
}
main();