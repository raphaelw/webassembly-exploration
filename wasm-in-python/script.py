from wasmer import engine, Store, Module, ImportObject, Function, FunctionType, Type, Instance

def python_number_printer(number):
    print("Python Number Printer", number)

store = Store()
# compile the module
with open('program.wasm', 'rb') as file:
    module = Module(store, file.read())

import_object = ImportObject()
host_function = Function(
    store,
    python_number_printer,
    FunctionType([Type.I32], []) # signature
)
import_object.register("env", { "external_number_printer": host_function } )
instance = Instance(module, import_object)

# call WASM function.
result = instance.exports.add(40, 2)
print(result)