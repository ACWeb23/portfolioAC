INCLUDE Irvine32.inc
.data
msg1 db "Hello World ",0
msg2 db "My Name Is Andrew ",0
.code
.code
	main PROC
	 mov edx, OFFSET msg1
	 call WriteString
	 mov al,0Dh
	 call WriteChar
	 mov al,0Ah
	 call WriteChar
	 mov edx, OFFSET msg2
	 call WriteString
	 exit
main ENDP
END main