#!/usr/bin/env python

import string
from pwn import *
context(terminal = ['bash'])

catalan = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452,]

def main():
    catana = process(['gdb', './catana'])

    log.info('Set Breakpoint 1')
    catana.recvuntil('(gdb)')
    #catana.sendline('break *0x000400556')
    catana.sendline('break *0x000400557')

    log.info('Set Breakpoint 2')
    catana.sendline('break *0x0004005d4')
    #catana.sendline('break *0x00400584')
    

    log.info('Running')
    catana.recvuntil('(gdb)')
    catana.sendline('run')

    catana.recvuntil('Starting program:')
    # RESULT FORMAT
    # (gdb) x/x $rbp-28
    # 0x7fffffffebb4:   0x00000000
    # (gdb) p/x $eax
    # $1 = 0x1
    while True:
        catana.recvuntil('Breakpoint 1')
        log.info('At Breakpoint 1')
        
        # var_14 = arg0;
        catana.recvuntil('(gdb)')
        catana.sendline('x/x $rbp-20')
        result = catana.recvline()
        arg0 = int(result.split(':')[1].strip(), 16)

        # var_18 = arg1;
        catana.recvuntil('(gdb)')
        catana.sendline('x/x $rbp-24')
        result = catana.recvline()
        arg1 = int(result.split(':')[1].strip(), 16)

        # var_1C = arg2;
        catana.recvuntil('(gdb)')
        catana.sendline('x/x $rbp-28')
        result = catana.recvline()
        arg2 = int(result.split(':')[1].strip(), 16)

        catana.recvuntil('(gdb)')
        catana.sendline('cont')
        # Alter contents
        #catana.recvuntil('(gdb)')
        #catana.sendline('set *((char *)$rbp-24) = ' + str(arg0))
        #catana.recvuntil('(gdb)')
        #catana.sendline('set *((char *)$rbp-28) = ' + str(arg0))

        # disable breakpoint to allow for recursion
        #catana.recvuntil('(gdb)')
        #catana.sendline('disable 1')

        log.info('Mid catalan({}, {}, {}) = {}'.format(arg0, arg1, arg2, '?'))        

        if 'Breakpoint 2' in catana.recvuntil('Breakpoint 2', timeout=0.2):
            log.info('At Breakpoint 2')

            # ret_val
            catana.recvuntil('(gdb)')
            catana.sendline('p/x $eax')
            result = catana.recvline()
            ret_val = int(result.split('=')[1].strip(), 16)

            # get result
            log.info('Found catalan({}, {}, {}) = {}'.format(arg0, arg1, arg2, ret_val))

            # enable back the breakpoint
            #catana.recvuntil('(gdb)')
            #catana.sendline('enable 1')

            # continue
            catana.recvuntil('(gdb)')
            catana.sendline('cont')

    catana.kill()


if __name__ == '__main__':
    main()
