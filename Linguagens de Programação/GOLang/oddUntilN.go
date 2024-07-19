package main
import ("fmt")

func main() {
    fmt.Println("Impressora de números impares até N")
	fmt.Println("Digite o n: ")
    var n int 
    fmt.Scanln(&n)
	var i int = 0
	for i < n {
		if i % 2 != 0 {
			fmt.Println(i)
			i++
		}
	}
}
