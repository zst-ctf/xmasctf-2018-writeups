#include <stdio.h>

int sub_400556(int arg0, int arg1, int arg2) {
    //printf("catalan(%d, %d, %d,)\n", arg0, arg1, arg2);
    if ((arg1 == arg0) && (arg2 == arg0)) {
        printf("catalan(%d, %d, %d) = %d\n", arg0, arg1, arg2, 1);
        return 0x1;
    } else {
        int var_8 = 0x0;
        if (arg1 < arg0) {
            var_8 = sub_400556(arg0, arg1 + 0x1, arg2);
        }
        if ((arg2 < arg0) && (arg2 < arg1)) {
            var_8 += sub_400556(arg0, arg1, arg2 + 0x1);
        }
        printf("catalan(%d, %d, %d) = %d\n", arg0, arg1, arg2, var_8);
        return var_8;
    }
    return 0;
}

int main()
{
    
    char str[500];
    for (int i = 0x0; i <= 0x6; i++) {
            for (int j = 0x0; j <= 0x23; j++) {
                str[8*i] += str[8*((i<<2)+(i<<3)+j)] * sub_400556(j, 0, 0);
            }
    }
        
    //int ret =  sub_400556(50,0,0);
    //printf("Ret %d\n", ret);
    printf("Ret %s\n", str);


    return 0;
}

