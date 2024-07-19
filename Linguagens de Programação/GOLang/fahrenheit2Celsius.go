
package main
import ("fmt")

func main() {
    fmt.Println("Conversos de Fahrenheit para Celsius")
	fmt.Println("Digite a temperatura em graus Fahrenheit: ")
    var n int 
    fmt.Scanln(&n)
	var Celsius int
	
	Celsius = (n - 32) * 5 / 9
	fmt.Println("A temperatura em Celsius é: ", Celsius)
}
