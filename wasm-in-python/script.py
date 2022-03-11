from wasmer import engine, Store, Module, ImportObject, \
                   Function, FunctionType, Type, Instance

def python_number_printer(number: int) -> None:
    print("Python Number Printer:", number)

store = Store()

# compile the module
with open("program.wasm", "rb") as file:
    module = Module(store, file.read())

# instantiate with imports
import_object = ImportObject()
import_object.register("env", {
    "external_number_printer": Function(store, python_number_printer)
})
instance = Instance(module, import_object)

# call WASM function
result = instance.exports.add(40, 2)
print("Result:", result)