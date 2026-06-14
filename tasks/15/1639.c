# Solved/*
    Solved by lfvbdghkjfgm
    https://lfvb.ru
*/

#include <stdio.h>

int main(void) {
    for (int a = 150000; a > 0; a --) {
        int flag = 1;
        for (int x = 1; x < 150000; x ++) {
            if (!(!(x % 512 == 0) || ((x % a == 0) || (x % 243 != 0)))) {
                flag = 0;
                break;
            }
        }
        if (flag) {
            printf("%d\n",a);
            break;
        }
    }

    return 0;
}

