; prog5.asm
; adding 2 values and looking at memory

INCLUDE Irvine32.inc
.data
cat dw  01h
dog dw  02h
sum dw   ?
.code
    main PROC
           
            call DumpRegs 
            mov ax,cat

            call DumpRegs 
            add ax,dog
 
            call DumpRegs 
            mov sum,ax
            
            mov esi, offset cat ; starting address 
            mov ecx, 20           ; number of bytes
            mov ebx,  1           ; data type 1=byte  2=word
            call DumpMem  
            exit
main ENDP
END main

