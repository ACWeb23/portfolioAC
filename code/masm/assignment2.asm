INCLUDE Irvine32.inc
.data
msg1 db "Hello I am Vir, A Synthetic Inteligence Tasked With Assisting You In Your Day.  ",0
.code
 main PROC
 mov edx, offset msg1 
 call WriteString 
 exit
main ENDP
END main

