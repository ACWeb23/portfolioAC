; prog8.asm  assemble with make32.bat
; how to output 1 character stored in register AL

INCLUDE Irvine32.inc
.data
.code
    main PROC
      mov al,41h           
      call WriteChar  ; write the char that is in the AL register
      exit
main ENDP
END main
