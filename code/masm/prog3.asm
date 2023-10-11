; Example prog3.asm
; assemble with make32.bat
; looking at memory

INCLUDE Irvine32.inc
.data
msg1    db "Hello World",0
.code
    main PROC
            mov esi, offset msg1 ; starting address 
            mov ecx, 20           ; number of bytes
            mov ebx,  1           ; data type 1=byte  2=word
            call DumpMem  
            exit
main ENDP
END main
