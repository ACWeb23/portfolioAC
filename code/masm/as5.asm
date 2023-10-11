INCLUDE Irvine32.inc
.data
msg1 db "Enter a number: ",0
msg2 db "Enter another number: ",0
msg3 db "The sum is: ",0
msg4 db "Jump ",0
msg5 db "Add ",0
msg6 db "Compare ",0
num1 db ?
num2 db ?
num3 db 0Ah
sum db ?
.code
main PROC
    mov edx,OFFSET msg1
    call WriteString
    call ReadChar
    call DumpRegs
    mov num1, al
    sub num1,30h
    
    mov edx,OFFSET msg2
    call WriteString
    call ReadChar
    call DumpRegs
    mov num2,al
    sub num2,30h
    
    mov edx,OFFSET msg5
    call WriteString
    mov al,num1
    add al,num2 ; add the two numbers
    call DumpRegs
    
    mov edx,OFFSET msg6
    call WriteString
    mov sum,al
    cmp sum,num3
    call DumpRegs
    js less

    mov edx,OFFSET msg4
    call WriteString
    mov edx,OFFSET msg3 ; print msg3
    call WriteString
    mov al,31h ; 
    call WriteChar 
    mov al,sum
    sub al,0Ah
    add al,30h
    call WriteChar
    jmp exit_program
less:  
    add al,30h ; 
    mov edx,OFFSET msg3 ; print msg3
    call WriteString
    call WriteChar ; print the sum
    jmp exit_program
    
exit_program:
    call Crlf
    call WaitMsg
    exit
main ENDP
END main
