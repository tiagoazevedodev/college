
#include <stdio.h>

int main()
{
    int n; int i; int total;
    printf("\tVerificador de numero primo\n");
    printf("Insira o numero que para ser verificado:");
    scanf("%d", &n);
    
    total = 0;
    for (i = n-1 ; i > 1 ; i--) {
        if (n % i == 0){
            total++;
        }
    }
    
    if (total) {
        printf("O numero %d não é primo.\n", n);
        return 0;
    } 
    
    printf("O numero %d é primo.\n", n);
    return 0;
}
