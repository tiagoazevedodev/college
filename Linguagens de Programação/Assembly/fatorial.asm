%include "io.inc"
section .text
global main

main:
    mov     eax, 5      ; Defina o número cujo fatorial deve ser calculado
    call    factorial   ; função para calcular o fatorial

    PRINT_UDEC 4, eax
    
factorial:
    mov     ebx, 1      ; Iniciei o fatorial como 1
    mov     ecx, eax    ; Usei ecx para contar até o valor de eax (cujo fatorial está sendo calculado)

calculate:
    imul    ebx, ecx    ; Multiplica ebx pelo contador (ecx)
    loop    calculate   ; Repita até que ecx seja zero

    mov     eax, ebx    ; O resultado final está em ebx, então movemos para eax para retornar
    ret
