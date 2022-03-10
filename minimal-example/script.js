// script.js
async function main() {
    const source = fetch('program.wasm');
    const { instance } = await WebAssembly.instantiateStreaming(source);

    const result = instance.exports.add(40, 2);
    console.log('Result: ' + result);
}
main();