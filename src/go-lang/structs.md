# This is my basic understanding of structs

Structures or structs are a group of several varibles in one place. They define how an object is defined much like class variables in other languages.

```go
package main

import(
  "fmt"
)

type Foo struct{
  bar string 
  bar2 int
}

func main(){
  f := foo{bar: "bar", bar2: "bar2"}
fmt.Println(p)
}
```

output: `{bar bar2}`
