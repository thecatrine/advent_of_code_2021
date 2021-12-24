#include <stdio.h>
#include <stdlib.h>


int test_num(int* num) {
    int w = 0; int x = 0; int y = 0; int z = 0;

    w = *num;num++;
    z = w;
    x = w + 17;

    w = *num;num++;
    z = 26*z + w + 31;
    x = (w + 5) % 26 + 10;

    w = *num;num++;
    z = 26*z + w + 19;
    x = (w + 19) % 26 + 15;

    w = *num;num++;
    z = 26*z + w + 14;
    x = (w + 14) % 26 - 8; // 1,2,3 possible

    w = *num;num++;
    z /= 26;
    if (x != w) {
        z = 26*z + w + 1;
    }
    x = z % 26 - 10;

    w = *num;num++;
    z /= 26;
    if (x != w) {
        z = 26*z + w + 20;
    }
    x = z % 26 + 11;

    w = *num;num++;
    if (x != w) {
        z = 26*z + w + 1;
    }
    x = z % 26 - 3;

    w = *num;num++;
    z /= 26;
    if (x != w) {
        z = 26*z + w + 18;
    }
    x = z % 26 + 14;

    w = *num;num++;
    if (x != w) {
        z = 26*z + w + 3;
    }
    x = z % 26 - 4;

    w = *num;num++;
    z /= 26;
    if (x != w) {
        z = 26*z + w + 22;
    }
    x = z % 26 + 14;

    w = *num;num++;
    if (x != w) {
        z = 26*z + w + 5;
    }
    x = z % 26 - 5;

    w = *num;num++;
    z /= 26;
    if (x != w) {
        z = 26*z + w + 3;
    }
    x = z % 26 - 11;

    w = *num;num++;
    z /= 26; // z < 26

    if (x != w) { // x == w
        z = 26*z + w + 10; // can't happen
    }

    if (z == 0) {return 1;} else {return 0;}
}

int main() {
    int num[14] = {9,9,9,9,9,9,9,9,9,9,9,9,9,9};
    uint count = 0;

    while (1) {
        int i = 13;
        int go = 1;
        while (go == 1) {
            num[i]--;
            if (num[i] == 0) {
                num[i] = 9;
                i--;
            } else {
                go = 0;
            }
        }
        if (count % 10000000 == 0) {
            printf("%d%d%d%d%d%d%d%d%d%d%d%d%d%d\n", num[0], num[1], num[2], num[3], num[4], num[5], num[6], num[7], num[8], num[9], num[10], num[11], num[12], num[13]);
        }
        count++;
        if (test_num(num) != 0) {
            printf("%d%d%d%d%d%d%d%d%d%d%d%d%d%d\n", num[0], num[1], num[2], num[3], num[4], num[5], num[6], num[7], num[8], num[9], num[10], num[11], num[12], num[13]);
            printf("%d\n\n", test_num(num));
            exit(1);
        }
    }
}