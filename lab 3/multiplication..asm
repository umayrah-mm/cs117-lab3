section .data
    msg db 'Result: '
    msgLen equ $ - msg

    result db 0          ; To hold the ASCII digit
    newline db 10        ; Newline character ('\n')

section .text
    global _start

_start:
    ; Load values into AL and BL
    mov al, 2            ; First number
    mov bl, 3            ; Second number

    ; Multiply AL * BL → result in AL
    mul bl               ; AL = AL * BL = 6

    ; Convert AL to ASCII
    add al, '0'          ; 6 → '6'
    mov [result], al     ; Store ASCII character

    ; Print "Result: "
    mov eax, 4           ; sys_write
    mov ebx, 1           ; File descriptor (stdout)
    mov ecx, msg         ; Pointer to message
    mov edx, msgLen      ; Length of message
    int 0x80

    ; Print result digit
    mov eax, 4
    mov ebx, 1
    mov ecx, result
    mov edx, 1
    int 0x80

    ; Print newline
    mov eax, 4
    mov ebx, 1
    mov ecx, newline
    mov edx, 1
    int 0x80

    ; Exit program
    mov eax, 1           ; sys_exit
    mov ebx, 0           ; Exit code
    int 0x80

