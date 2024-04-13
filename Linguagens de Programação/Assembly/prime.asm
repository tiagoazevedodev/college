%include "io.inc"
section .text
global main

main:
    mov     eax, 2         ; Número a ser testado
    mov     ebx, 0         ; contagem de divisores
    mov     ecx, 2         ; Iniciando o divisor em 2

check_divisor:
    cmp     ecx, eax       ; testa se o divisor excede o número
    jg      end_check      ; Se sim, para
    mov     edx, 0         ; Limpa edx para dividir
    div     ecx            ; Divide eax pelo divisor
    test    edx, edx       ; Verifica se tem resto
    jz      not_prime      ; Se não tiver resto, não é primo
    inc     ecx            ; Incrementa o divisor
    jmp     check_divisor  ; Verifica o próximo divisor

not_prime:
    mov     ebx, 1         ; Define ebx como 1 para indicar que não é primo
    jmp     end_check      ; Termina a verificação

end_check:
    cmp     ebx, 0         ; Verifica o valor de ebx
    je      prime_output   ; Se ebx for 0, o número é primo
    mov     eax, 0         ; Caso contrário, define eax como 0 para indicar que não é primo
    PRINT_STRING "O numero nao e primo"
    jmp     exit_program   ; termina

prime_output:
    PRINT_STRING "O numero e primo"
    mov     eax, 1         ; Define eax como 1 para indicar que é primo
exit_program:
    ret
