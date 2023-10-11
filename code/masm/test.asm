; Example test.asm
; assemble with make32.bat
; looking at memory

INCLUDE Irvine32.inc
.data
msg1    db "Hello World",0
.code
    main PROC
            mov edx, offset msg1 ; starting address 
            call WriteString     ; printing routine
            exit
main ENDP
END main
