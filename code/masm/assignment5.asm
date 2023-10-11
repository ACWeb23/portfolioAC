INCLUDE Irvine32.inc

.data
msg1 db "Enter a number: ",0
msg2 db "Enter another number: ",0
msg3 db "The sum is: ",0
num1 dw ?
num2 dw ?
sum dw ?
.code
main PROC
    mov edx,OFFSET msg1
    call WriteString
    call ReadInt
    mov num1, ax
    
    mov edx,OFFSET msg2
    call WriteString
    call ReadInt
    mov num2,ax
    
    mov ax,num1
    add ax,num2 ; add the two numbers
    
    mov sum,ax
    cmp sum,10
    jge greater_or_equal
    
    
less:
    add ax,30h ; 
    mov edx,OFFSET msg3 ; print msg3
    call WriteString
    call WriteChar ; print the sum
    jmp exit_program

greater_or_equal:
    mov edx,OFFSET msg3 ; print msg3
    call WriteString
    mov al,31h ; 
    call WriteChar 
    mov ax,sum
    sub ax,10
    add ax,30h
    call WriteChar
    jmp exit_program

    
exit_program:
    call Crlf
    call WaitMsg
    exit
main ENDP
END main
