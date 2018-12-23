#!/usr/bin/env python3
import subprocess

# Open up file as bytes
with open("out_file3", "rb") as f:
    file = f.read()

#size = 0x5042
#while size > 0x43e8:
#    size -= 1

size = 0x43e8
while size < 100000:
    size += 1

    # try to fix by truncating
    with open("out_fixed", "wb") as f:
        f.write(file[:size])

    # check if working
    command = ["objdump", "-d", "out_fixed"]
    #command = ["./out_fixed"]
    results = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True)
    results = results.stderr

    print(results)

    #if size == 19328:
    #    quit()

    '''
    if len(results.strip()) == 0 or 'Segmentation fault' in results:
        print("SegFault:", size)
        continue
    '''
    if 'file format not recognized' in results or 'file truncated' in results:
        print("Failed size:", size)
        continue
    else:
        print("SUCCESS size:", size)
        quit()

print("End")