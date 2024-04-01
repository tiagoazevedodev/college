
#include <stdio.h>

int
main ()
{
    
int n, i, fatorial;

printf("Insira o número que você quer o Fatorial:");
scanf("%d", &n);

fatorial = n;
for (i=1;i < n; i++){
    fatorial *= i;
}
printf("O fatorial de %d é %d", n, fatorial);
    
  return 0;
}
