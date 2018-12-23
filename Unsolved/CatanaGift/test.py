import functools


# memoize
@functools.lru_cache(maxsize=None)
def sub_400556(arg0, arg1, arg2):
    #print
    #printf("sub_400556(%d, %d, %d,)\n", arg0, arg1, arg2);
    if ((arg1 == arg0) and (arg2 == arg0)):
        return 0x1
    else:
        var_8 = 0x0;
        if (arg1 < arg0):
            var_8 = sub_400556(arg0, arg1 + 0x1, arg2);

        if ((arg2 < arg0) and (arg2 < arg1)):
            var_8 += sub_400556(arg0, arg1, arg2 + 0x1);
        return var_8;

    return 0;


s = [0] * 1024
def main():
    for i in range(0x06 + 1):
        for j in range(0x23 + 1):
            s[8*i] += s[8*((i<<2)+(i<<3)+j)] * sub_400556(j, 0, 0);
        
    #//int ret =  sub_400556(50,0,0);
    #//printf("Ret %d\n", ret);
    #printf("Ret %s\n", str);
    print (s)

if __name__ == '__main__':
    main()