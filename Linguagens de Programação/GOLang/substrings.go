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

    re := regexp.MustCompile(m)

    count := re.FindAllStringIndex(n, -1)

    fmt.Println("A palavra", m, "ocorre ", len(count), " vezes na frase.")
}
