// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream> // for getch() function
int sub1(int, int, int);
int main()
{
    int a, b, c, iret;
    a = 1; 
    b = 2; 
    c = 3;
    iret = sub1(a, b, c);
    std::cout << iret << '\n';
    return 0;
}
int sub1(int a, int b, int c)
{
    int d;
    d = a + b + c;
    return d;
}
// This program above would be compiled as :
int second(int a, int b, int c)
{
    __asm {
        .DATA
        a DW ? ; define variables for main 16 but
        b DW ? ; 16 bit value
        c DW ? ; 16 bit valus
        iret DW ?
        sub1_a DW ? ; define local variables for sub1
        sub1_b DW ?
        sub1_c DW ?
        sub1_d DW ?
        sub1_ret DD ? ; Define 32 bit variable to store the return address
        .CODE
        main PROC
        PUSH A; push value A onto the stack
        PUSH B; push value B onto the stack
        PUSH C; push value c onto the stack
        CALL SUB1; call procedure sub1
        POP D; get the return value
        //<print valueand end>
        main ENDP
        sub_1 PROC; begin procedure
        pop sub1_ret; pop return address and save in sub1_ret
        pop sub1_c; pop cand save in sub1_c
        pop sub1_b; pop band save in sub1_b
        pop sub1_a; pop aand save in sub1_a
        mov ax, sub1_a; d = a + b + c
        add ax, sub1_b
        add ax, sub1_c
        mov sub1_d, ax
        push sub1_d; push return value on stack
        push sub1_ret; push return address back on stack
        ret
        sub_1 ENDP; end procedure
        END main
    };
}
