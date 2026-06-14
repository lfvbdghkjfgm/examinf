# Solved/* 
    Solved by lfvbdghkjfgm
    https://lfvb.ru
*/
#include <stdio.h>

int g(int n) {
    if (n <= 9) {
        return 3 * n;
    }
    return g(n - 4) + 2;
}

int f(int n) {
    return g(n-1) + g(n - 3);
}

int main(void) {
    printf("%d",f(42999));

    return 0;
}

