
#include <stdio.h>

int main()
{
    int n;
    printf("\tConversor de Fahrenheit para Celsius\n");
    printf("Insira a temperatura em Fahrenheit:");
    scanf("%d", &n);
    float celsius = ((n - 32) * 5) / (float)9;
    
    printf("A temperatura %d em celsius é: %.1f", n, celsius);
    
    return 0;
}
