; Prog7.asm assemble with make32.bat
; how to input 1 character 
INCLUDE Irvine32.inc
.data
msg1    db "Enter a key  ",0
.code
    main PROC
            mov  edx, OFFSET msg1
            call WriteString
           call ReadChar   ; char is placed in the AL register
           call DumpRegs
           exit
main ENDP
END main
