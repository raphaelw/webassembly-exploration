# imported-function

Call a JavaScript function from WebAssembly module written in C.

**Compile to wasm file with:**

```sh
clang --target=wasm32 --no-standard-libraries -Wl,--export-all -Wl,--no-entry -Wl,--allow-undefined -o program.wasm program.c
```