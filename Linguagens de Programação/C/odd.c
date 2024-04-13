
#include <stdio.h>

int main()
{
    int n;
    printf("\tPrintador de numeros impares\n");
    printf("Insira o numero de impares a serem imprimidos:");
    scanf("%d", &n);
    int inicial = n; int i = 1;
    while (n >= 1){
        if (i % 2 != 0){
            n--;
            printf("numero %d: %d\n", inicial - n, i);
        }
        i++;
    }
    return 0;
}
