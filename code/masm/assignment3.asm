INCLUDE Irvine32.inc
.data
msg1 db "Enter A Key ",0
.code
 main PROC
mov edx, OFFSET msg1
call WriteString
call ReadChar

 call DumpRegs
 exit
main ENDP
END main
