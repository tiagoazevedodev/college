package main
import (
    "fmt"
    "regexp"
)

func main() {
    fmt.Println("Detector de quantidade de palavras em uma frase")
    fmt.Println("Digite a frase: ")
    var n string
    fmt.Scanln(&n)
    fmt.Println("Digite a palavra: ")
    var m string
    fmt.Scanln(&m)

    // Cria uma expressão regular para buscar a palavra 'm' na frase 'n'
    re := regexp.MustCompile(m)

    // Conta o número de ocorrências da palavra na frase
    count := re.FindAllStringIndex(n, -1)

    fmt.Println("A palavra", m, "ocorre ", len(count), " vezes na frase.")
}
