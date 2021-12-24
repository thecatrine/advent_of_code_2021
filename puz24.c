#include <stdio.h>
#include <stdlib.h>


int test_num(int* num) {
    int w = 0; int x = 0; int y = 0; int z = 0;

    w = *num;num++;
    x = 13;
    if (x != w) {
        z *= 26;
        z += w + 30;
    }
    

    w = *num;num++;
    x = z % 26;
    x += 13;
    if (x != w) {
        z *= 26;
        z += w + 31;
    }


    w = *num;num++;
    x = z % 26;
    x += 10;
    if (x != w) {
        z *= 26;
        z += w + 19;
    }

    w = *num;num++;
    x = z % 26;
    x += 15;
    if (x != w) {
        z *= 26;
        z += w + 14;
    }

    w = *num;num++;
    x = z % 26;
    z /= 26;
    x += -8;
    if (x != w) {
        z *= 26;
        z += w + 1;
    }

    w = *num;num++;
    x = z % 26;
    z /= 26;
    x += -10;
    if (x != w) {
        z *= 26;
        z += w + 20;
    }

    w = *num;num++;
    x = z % 26;
    x += 11;
    if (x != w) {
        z *= 26;
        z += w + 1
    }

    w = *num;num++;
    x = z % 26;
    z /= 26;
    x += -3;
    if (x != w) {
        z *= 26;
        z += w + 18;
    }


    w = *num;num++;
    x = z % 26;
    x += 14;
    if (x != w) {
        z *= 26;
        z += w + 3;
    }

    

    w = *num;num++;
    x = z % 26;
    z /= 26;
    x += -4;
    if (x != w) 
        z *= 26;
        z += 22 + w;
    }


    w = *num;num++;
    x = z % 26;
    x += 14;
    if (x != w) {
        z *= 26;
        z += w + 5;
    }

    w = *num;num++;
    
    x = z % 26;
    z /= 26;
    x += -5;
    if (x != w) {
        x = 1;
        z *= 26;
    
        z += w + 13;
    }
    w = *num;num++; // 13th not used

    x = z % 26;


    x -= 8;
    z = 0;
    x -= 11;
    
    w = *num;num++;
    if (x == w) {        
        z += w;
    } else {
        z *= 26;
        z += w + 10;
    }


    if (z == 0) {return 1;} else {return 0;}
}

int main() {
    int num[14] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    uint count = 0;

    while (1) {
        int i = 0;
        int go = 1;
        while (go == 1) {
            num[i]++;
            if (num[i] == 10) {
                num[i] = 1;
                i++;
            } else {
                go = 0;
            }
        }
        if (test_num(num) != 0) {
            printf("%d%d%d%d%d%d%d%d%d%d%d%d%d%d\n", num[0], num[1], num[2], num[3], num[4], num[5], num[6], num[7], num[8], num[9], num[10], num[11], num[12], num[13]);
            printf("%d\n\n", test_num(num));
        }
    }
}