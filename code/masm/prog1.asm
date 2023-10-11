; Example:   prog1.asm
; assemble with make32.bat
; looking at the registers 
;                            
INCLUDE Irvine32.inc
.data
.code
    main PROC
     call DumpRegs
     exit
main ENDP
END main
