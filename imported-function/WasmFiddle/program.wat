(module
 (type $FUNCSIG$vi (func (param i32)))
 (import "env" "external_number_printer" (func $external_number_printer (param i32)))
 (table 0 anyfunc)
 (memory $0 1)
 (export "memory" (memory $0))
 (export "add" (func $add))
 (func $add (; 1 ;) (param $0 i32) (param $1 i32) (result i32)
  (call $external_number_printer
   (tee_local $1
    (i32.add
     (get_local $1)
     (get_local $0)
    )
   )
  )
  (get_local $1)
 )
)
