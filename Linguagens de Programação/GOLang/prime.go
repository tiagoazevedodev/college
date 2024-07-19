package main
import ("fmt")

func main() {
    fmt.Println("Calculadora de número primo")
	fmt.Println("Digite o número de Base: ")
    var n int 
    fmt.Scanln(&n)
	var result bool = true
	for i := 2; i < n; i++ {
		if n % i == 0 {
			result = false
			break
		}
	}
	if result {
		fmt.Println("O número é primo")
	} else {
		fmt.Println("O número não é primo")
	}
}
