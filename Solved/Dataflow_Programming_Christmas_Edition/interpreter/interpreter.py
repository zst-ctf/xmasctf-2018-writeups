#!/usr/bin/env python3
import sys

def debug_print(*arg):
    pass

# Comment this to disable debugging messages
debug_print = print

# registers to hold the input left/right
register_left = dict()
register_right = dict()

index_levels = []

def execute_line(line):
    # Instruction: {index} {operator} {destination}
    # Table: Operand | Left input | Right input | Left output | Right output
    items = line.split(' ')
    index = int(items[0])
    operator = items[1]
    try:
        output_left = items[2]
        output_right = items[3]
    except:
        # ignore if no output items
        pass

    next_index = index + 1

    # for instructions that allow passing of empty inputs
    empty_left_input = (index not in register_left or register_left[index] == None)
    empty_right_input = (index not in register_right or register_right[index] == None)
    # both_empty_inputs = empty_left_input and empty_right_input
    either_empty_inputs = empty_left_input or empty_right_input

    #####################################################
    # 1. Input/Output operators:
    if operator == 'REA':
        # REA (Reads integer from input)
        # REA None None Integer None
        result = int(input().strip())
        place_output(result, output_left)
    elif operator == 'PRI':
        # PRI (Prints 8-bit integer to output)
        # PRI Integer None None None
        integer = register_left[index]
        if empty_left_input:
            raise Exception("Empty print input", integer)
        print(integer, end='')
    elif operator == 'PRC':
        # PRC (Prints character to output)
        # PRC Integer None None None
        character = chr(register_left[index])
        if empty_left_input:
            raise Exception("Empty print input", character)
        print(character, end='')

    #####################################################
    # 2. Arithmetic operators:
    elif operator == 'ADD':
        # ADD (Adds two integers)
        # ADD Integer Integer Integer None
        a = register_left[index]
        b = register_right[index]
        result = (a + b)
        place_output(result, output_left)
    elif operator == 'SUB':
        # SUB (Subtracts two integers)
        # SUB Integer Integer Integer None
        a = register_left[index]
        b = register_right[index]
        result = (a - b)
        place_output(result, output_left)
    elif operator == 'MUL':
        # MUL (Multiplies two integers)
        # MUL Integer Integer Integer None
        a = register_left[index]
        b = register_right[index]
        result = (a * b)
        place_output(result, output_left)
    elif operator == 'DIV':
        # DIV (Divides two integers and returns quotient and remainder)
        # DIV Integer Integer Integer (quotient) Integer (remainder)
        a = register_left[index]
        b = register_right[index]
        quotient = a // b
        remainder = a % b
        place_output(quotient, output_left)
        place_output(remainder, output_right)

    #####################################################
    # 3. Boolean arithmetic operators:
    elif operator == 'AND':
        # AND (Boolean AND operator)
        # AND Boolean Boolean Boolean None
        a = (register_left[index] != 0)
        b = (register_right[index] != 0)
        result = 1 if (a and b) else 0
        place_output(result, output_left)
    elif operator == 'ORR':
        # ORR (Boolean OR operator)
        # ORR Boolean Boolean Boolean None
        a = (register_left[index] != 0)
        b = (register_right[index] != 0)
        result = 1 if (a or b) else 0
        place_output(result, output_left)
    elif operator == 'XOR':
        # XOR (Boolean XOR operator)
        # XOR Boolean Boolean Boolean None
        a = (register_left[index] != 0)
        b = (register_right[index] != 0)
        result = 1 if (a ^ b) else 0
        place_output(result, output_left)
    elif operator == 'NOT':
        # NOT (Boolean NOT operator)
        # NOT Boolean None Boolean None
        a = (register_left[index] != 0)
        result = 1 if (not a) else 0
        place_output(result, output_left)

    #####################################################
    # 4. Comparison operators:
    elif operator == 'SML':
        # SML (Smaller comparison operator)
        # SML Integer Integer Boolean None
        a = register_left[index]
        b = register_right[index]
        result = 1 if (a < b) else 0
        place_output(result, output_left)
    elif operator == 'SME':
        # SME (Smaller or equal comparison operator)
        # SME Integer Integer Boolean None
        a = register_left[index]
        b = register_right[index]
        result = 1 if (a <= b) else 0
        place_output(result, output_left)
    elif operator == 'GRT':
        # GRT (Greater comparison operator)
        # GRT Integer Integer Boolean None
        a = register_left[index]
        b = register_right[index]
        result = 1 if (a > b) else 0
        place_output(result, output_left)
    elif operator == 'GRE':
        # GRE (Greater or equal comparison operator)
        # GRE Integer Integer Boolean None
        a = register_left[index]
        b = register_right[index]
        result = 1 if (a >= b) else 0
        place_output(result, output_left)
        debug_print(f"Line {index}: {a} >= {b} : {result}")
    elif operator == 'EQU':
        # EQU (equal comparison operator)
        # EQU Integer Integer Boolean None
        a = register_left[index]
        b = register_right[index]
        result = 1 if (a == b) else 0
        debug_print(f"*** EQU {a} == {b} : {result}")
        place_output(result, output_left)
    elif operator == 'DIF':
        # DIF (different comparison operator)
        # DIF Integer Integer Boolean None
        a = register_left[index]
        b = register_right[index]
        result = 1 if (a != b) else 0
        place_output(result, output_left)

    #####################################################
    # 5. Conditional operator:
    elif operator == 'BRB':
        # BRB (Branch on boolean)
        # BRB Any Boolean Any (if true) Any (if false)
        in_item = register_left[index]
        branch = register_right[index]
        if branch != 0:
            place_output(in_item, output_left)
            place_output(None, output_right)
            debug_print(f"BRB: {in_item} -> LEFT {branch} -> {output_left}")
        else:
            place_output(None, output_left)
            place_output(in_item, output_right)
            debug_print(f"BRB: {in_item} -> RIGHT {branch} -> {output_right}")

    #####################################################
    # 6. Bitwise operators:
    elif operator == 'SHR':
        # SHR (Shift to the right)
        # SHR Integer Integer Integer None
        num = register_left[index]
        shift = register_right[index]
        result = (num >> shift) & 0xFF
        place_output(result, output_left)
    elif operator == 'SHL':
        # SHL (Shift to the left)
        # SHL Integer Integer Integer None
        num = register_left[index]
        shift = register_right[index]
        result = (num << shift) & 0xFF
        place_output(result, output_left)
    elif operator == 'BAN':
        # BAN (Bitwise AND)
        # BAN Integer Integer Integer None
        a = register_left[index]
        b = register_right[index]
        result = a & b
        place_output(result, output_left)
    elif operator == 'BOR':
        # BOR (Bitwise OR)
        # BOR Integer Integer Integer None
        a = register_left[index]
        b = register_right[index]
        result = a | b
        place_output(result, output_left)
    elif operator == 'BXR':
        # BXR (Bitwise XOR)
        # BXR Integer Integer Integer None
        a = register_left[index]
        b = register_right[index]
        result = a ^ b
        place_output(result, output_left)
    elif operator == 'BNT':
        # BNT (Bitwise NOT)
        # BNT Integer None Integer None
        a = register_left[index]
        result = 0xFF ^ a  # 8-bits bitwise NOT
        place_output(result, output_left)

    #####################################################
    # 7. Index level control operators:
    elif operator == 'AIL':
        # AIL (Add to index level)
        # AIL Any Integer Any None

        # if empty inputs, then ignore
        if (either_empty_inputs):
            debug_print(f"AIL Empty: {line}")
            pass
        else:
            debug_print(f"AIL {index}L: {register_left[index]}")
            a = register_left[index]
            b = register_right[index]  # index level
            # Add index level to output after doing addition
            il = place_output(a, output_left)
            #index_out = get_output_index(output)
            index_levels.append(il)

    elif operator == 'SIL':
        # SIL (Subtract from index level)
        # SIL Any Integer Any None

        # if empty inputs, then ignore
        if (either_empty_inputs):
            debug_print(f"AIL Empty: {line}")
            pass
        else:
            a = register_left[index]
            b = register_right[index]
            # Add index level to output after doing addition
            il = place_output(a, output_left)
            index_levels.append(il)

    #####################################################
    # 8. DataFlow specific operators:
    elif operator == 'CLN':
        # CLN (Clones input)
        # CLN Any None Any Any
        a = register_left[index]
        place_output(a, output_left)
        place_output(a, output_right)

    elif 'SND_' in operator:
        # SND_X (Send a constant to the input layer of another node, X is
        # an 8-bit integer
        # SND X None None Integer None
        if check_output_empty(output_left):
            constant = int(operator.split('_')[1])
            place_output(constant, output_left)
        else:
            debug_print(f"Skip: {line}")

    else:
        raise Exception(f'Unimplemented operator: {operator}')

    # empty register after each run?
    # register_left[index] = None
    # register_right[index] = None

    '''
    # if 158 in register_left and register_left[158] != None:
    #    debug_print("*** 158L", register_left[158])
    if 13 in register_left:
        debug_print("*** 13L", register_left[13])
    if 11 in register_left:
        debug_print("*** 11L", register_left[11])
    if 11 in register_right:
        debug_print("*** 11R", register_right[11])
    '''

    return next_index


def get_output_index(name):
    return int(name.replace('L', '').replace('R', ''))


def check_output_empty(output):
    index = get_output_index(output)
    empty_left = (index not in register_left or register_left[index] == None)
    empty_right = (index not in register_right or register_right[index] == None)
    if 'L' in output:
        return empty_left
    elif 'R' in output:
        return empty_right


def place_output(item, output):
    if output == '−' or output == '-':
        # raise Exception(f'Place into empty output: {item} -> {output}')
        # Some operations have empty outputs which are intended
        return

    index_out = get_output_index(output)
    if 'L' in output:
        register_left[index_out] = item
    elif 'R' in output:
        register_right[index_out] = item
    return index_out


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        contents = f.read().splitlines()

    index = 0
    while True:
        line = contents[index]
        try:
            debug_print(f"Execute {line}")
            next_index = execute_line(line)
            # if already going through index level
            if index in index_levels:
                index_levels.remove(index)
            # if last instruction is successful
            if next_index == len(contents):
                break;
        except Exception as e:
            # raise e
            debug_print(f"Index {index}, skipping due to empty inputs,", e)
            next_index = index + 1

        index = next_index

        # If at the end of the program,
        # check if there's any index
        # levels to re-execute
        if index >= len(contents):
            try:
                index = next_index = index_levels.pop(0)
                debug_print(f"Hop {next_index}")
            except IndexError as e:
                debug_print(f"Empty Index, skip {next_index}", e)
                break;            

    print("\n>> Done")
