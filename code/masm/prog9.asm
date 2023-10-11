; prog9.asm
; assemble with make32.bat
; how to input 1 character and output 1 character

INCLUDE Irvine32.inc
.data
msg1    db "Enter a key  ",0
msg2    db "You typed in ",0
.code
    main PROC
         
            mov         edx, OFFSET msg1
            call        WriteString
            call ReadChar   ; char is placed in the AL register

            mov         edx, OFFSET msg2
            call        WriteString
            call WriteChar  ; write the char that is in the AL register
            
            exit
main ENDP
END main
