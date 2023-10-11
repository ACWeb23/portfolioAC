;prog2.asm
; assemble with make32.bat
; looking at memory

INCLUDE Irvine32.inc
.data
cat  db 06h
dog  dw 1234h
mouse dw 1abch
.code
    main PROC
            mov esi, offset cat ; starting address 
            mov ecx, 20           ; number of bytes
            mov ebx,  1           ; data type 1=byte  2=word
            call DumpMem  
            exit
main ENDP
END main
