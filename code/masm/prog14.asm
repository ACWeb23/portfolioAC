; This is a comment anything to the right of a “;” is a comment
INCLUDE Irvine32.inc ;This is an “includes” file that will link in the supporting functions
 ; that we need
.DATA ;this is the data sections where we define data cells.
 ; We will discuss more about this later
cat db 10h ; memory cell “cat” is defined as a byte (8 bits) and contains the value 10(Hex)
mouse dw 1Ah ; memory cell “mouse” is defined as 2 bytes and contains 1A(Hex)
dog dw ? ; memory cell “dog” is defined and occupies 2 bytes (16 bits) and
 ;has no value yet
.CODE ; this is where code is placed
main PROC ; code goes here
 mov al,cat ; these are instructions which will be discussed later
 mov dog,bx
 add bx,mouse
exit
main ENDP ; end MAIN procedure
END main ; end the program
