#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* countAndSay(int n) {
    char* ret = malloc(10000000);
    char* tmp = malloc(10000000);
    ret[0] = '1';
    ret[1] = 0;
    int len = 1;
    // int val = 1;
    // itoa(val, ret, 10);
    int pos = 0;
    for (int i = 1; i < n; i++) {
        // int len = strlen(ret);
        char curr = ret[0];
        int acc = 1;
        // int num = 0;
        for (int j = 1; j < len; j++) {
            if (ret[j] != curr) {
                // num = num * 100 + acc * 10 + curr - '0';
                tmp[pos] = acc + '0';
                tmp[pos+1] = curr;
                curr = ret[j];
                pos+=2;
                acc = 1;
            } else {
                acc++;
            }
        }
        tmp[pos] = acc + '0';
        tmp[pos+1] = curr;
        tmp[pos+2] = 0;
        len = pos+2;
        pos = 0;
        memcpy(ret, tmp, len + 1);
        // itoa(num, ret, 10);
    }
    return ret;
}