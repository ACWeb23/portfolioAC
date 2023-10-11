INCLUDE Irvine32.inc
.data
msg1 db "Hello World",0
.code
 main PROC
 mov edx, OFFSET msg1
 call WriteString
 exit
main ENDP
END main