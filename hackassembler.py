import sys

###############################################################################

COMMENT_MARKER = '//'

COMP_INSTRUCTIONS = {
    '0'  : '0101010',
    '1'  : '0111111',
    '-1' : '0111010',
    'D'  : '0001100',
    'A'  : '0110000',
    'M'  : '1110000',
    '!D' : '0001101',
    '!A' : '0110001',
    '!M' : '1110001',
    '-D' : '0001111',
    '-A' : '0110011',
    '-M' : '1110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'M+1': '1110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'M-1': '1110010',
    'D+A': '0000010',
    'D+M': '1000010',
    'A+D': '0000010',
    'M+D': '1000010',
    'D-A': '0010011',
    'D-M': '1010011',
    'A-D': '0000111',
    'M-D': '1000111',
    'D&A': '0000000',
    'D&M': '1000000',
    'A&D': '0000000',
    'M&D': '1000000',
    'D|A': '0010101',
    'D|M': '1010101',
    'A|D': '0010101',
    'M|D': '1010101',
}

DEST_INSTRUCTIONS = {
    None : '000',
    'M'  : '001',
    'D'  : '010',
    'MD' : '011',
    'A'  : '100',
    'AM' : '101',
    'AD' : '110',
    'AMD': '111',
}

JUMP_INSTRUCTIONS = {
    None : '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

###############################################################################

allocation_address = 16

symbols = {
    **{f'R{i}': i for i in range(16)},
    'SCREEN': 16384,
    'KBD'   : 24576,
    'SP'    : 0,
    'LCL'   : 1,
    'ARG'   : 2,
    'THIS'  : 3,
    'THAT'  : 4,
}

###############################################################################

def remove_whitespace(code):
    for line in code:
        if COMMENT_MARKER in line:
            line = line.split(COMMENT_MARKER)[0].strip()
        if not line:
            continue
        else:
            yield line.replace(' ', '')

def process_labels(code):
    i = 0
    for line in code:
        if line[0] == '(' and line[-1] == ')':
            label = line[1:-1]
            if label in symbols:
                raise ValueError(f'Duplicate label "{label}"')
            else:
                symbols[label] = i
        else:
            i += 1
            yield line

def preprocess_code(code):
    code = remove_whitespace(code)
    code = process_labels(code)
    return list(code)

###############################################################################

def allocate_variable(symbol):
    global allocation_address
    symbols[symbol] = allocation_address
    allocation_address += 1
    return symbols[symbol]

def translate_a_statement(line):
    try:
        address = int(line[1: ])
    except ValueError:
        symbol = line[1: ]
        if symbol in symbols:
            address = symbols[symbol]
        else:
            address = allocate_variable(symbol)
    address = bin(address)[2: ]
    return '0' * (16 - len(address)) + address

def translate_c_statement(line):
    dest, jump = None, None
    if '=' in line:
        dest, line = line.split('=')
    if ';' in line:
        comp, jump = line.split(';')
    else:
        comp = line
    instruction = '111'
    try:
        instruction += COMP_INSTRUCTIONS[comp]
        instruction += DEST_INSTRUCTIONS[dest]
        instruction += JUMP_INSTRUCTIONS[jump]
    except KeyError:
        raise ValueError()
    return instruction

def translate_code(code):
    machine_code = ''
    for num, line in enumerate(code):
        if line[0] == '@':
            machine_code += translate_a_statement(line)
        else:
            try:
                machine_code += translate_c_statement(line)
            except ValueError:
                raise ValueError(f'Syntax error (line {num}): {line}')
        machine_code += '\n'
    return machine_code

###############################################################################

def main():
    input_filename = sys.argv[1]
    with open(input_filename, 'r') as f:
        raw_code = map(lambda x: x.strip(), f.read().split('\n'))
    prepped_code = preprocess_code(raw_code)
    machine_code = translate_code(prepped_code)
    output_filename = '.'.join(input_filename.split('.')[ :-1]) + '.hack'
    with open(output_filename, 'w') as f:
        f.write(machine_code)
    print(f'Wrote assembled program into {output_filename}')

if __name__ == '__main__':
    main()
