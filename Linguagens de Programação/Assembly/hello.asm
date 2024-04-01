.section .data
    msg:    .ascii "Hello, World!\n"
    len =   . - msg

.section .text
    .global _start

_start:
    # Escreve a string no stdout (tela)
    mov $1, %rax             # syscall número 1 (sys_write)
    mov $1, %rdi             # file descriptor 1 (stdout)
    mov $msg, %rsi           # endereço da string
    mov $len, %rdx           # tamanho da string
    syscall

    # Chama a syscall de saída do programa
    mov $60, %rax            # syscall número 60 (sys_exit)
    xor %rdi, %rdi           # código de saída 0
    syscall
