package main
import ("fmt")

func main() {
    fmt.Println("Calculadora de Expoente")
    var n int 
    var x int
	fmt.Println("Digite o número de Base: ")
    fmt.Scanln(&n)
	fmt.Println("Digite o expoente desejado: ")
	fmt.Scanln(&x)
    var result int = 1
    for i := 0; i < x; i++ {
        result *= n
    }
    fmt.Println("O resultado é: ", result)
}
