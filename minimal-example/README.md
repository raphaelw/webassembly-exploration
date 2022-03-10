# minimal-example

Call a WebAssembly module function from JavaScript.

**Compile to wasm file with:**

```sh
clang --target=wasm32 --no-standard-libraries -Wl,--export-all -Wl,--no-entry -o program.wasm program.c
```

Thanks to https://depth-first.com/articles/2019/10/16/compiling-c-to-webassembly-and-running-it-without-emscripten/