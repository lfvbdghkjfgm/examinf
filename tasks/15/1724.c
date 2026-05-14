
/*
    Solved by lfvbdghkjfgm
    https://lfvb.ru
*/

#include <stdio.h>

int main(void) {
    for (int a = 0; a < 131072; a ++) {
        int fl = 1;
        for (int x = 1; x <= 131072; x ++) {
            for (int y = 1; y <= 131072; y ++) {
                if (!((131072 != 2 * y + 8 * x) || (a > 2 * x) && (a > y))) {
                    fl = 0;
                    break;
                }
                if (2* y + 8 * x > 131072) {
                    break;
                }
            }
            if (fl == 0) {
                break;
            }
        }
        if (fl) {
            printf("%d",a);
            break;
        }
    }

    return 0;
}