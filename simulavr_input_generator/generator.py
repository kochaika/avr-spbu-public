import csv
import os
import sys
from port_address_mapping import port_to_address_map
out_folder = 'inputs'

def csv_reader(csv_path):
    res = []
    with open(csv_path, "r") as f_obj:
        reader = csv.reader(f_obj)
        for i in reader:
            res.append(list(i))
    return res

def str_to_bin(value):
    try:
        if value.find('0x') == 0:
            if int(value, 16) > 255:
                raise ValueError('Too big port value: {}'.format(value))
            return int(value, 16).to_bytes(1,byteorder='big')
        if value.find('0b') == 0:
            if int(value, 2) > 255:
                raise ValueError('Too big port value: {}'.format(value))
            return int(value, 2).to_bytes(1,byteorder='big')
    except ValueError:
        pass
    raise ValueError('Wrong port value: {}'.format(value))

def print_help(progname):
    print('''
    Usage:
        1. Create signal description file with one port description per line
        2. Call this program: python3 {} <filename>
        3. Run SimulAVR with keys to be displayed
    
    Signal description file example: 
        PINB,0b100,0b11,
        PORTA,0b00000000,0b01010101,0xAB,0xFF
        PORTC,0xAA,0xAB,0xFF
        <PORT_NAME>,<value in bin with 0b prefix> or <value in hex with 0x prefix>, ...
        
    Displayed keys example:
        -R 0x23,inputs/0x23.input -R 0x22,inputs/0x22.input -R 0x28,inputs/0x28.input 
    '''.format(progname))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        progname = sys.argv[0].split('/')[-1]
        print_help(progname)
        exit(0)
    source = csv_reader(sys.argv[1])
    commands = []
    os.makedirs(os.path.normpath(out_folder), exist_ok=True)

    for line in source:
        port_address = port_to_address_map[line[0]]
        filename = '{}/{}.input'.format(out_folder,port_address)
        f = open(filename, "wb")
        for val in line[1:]:
            f.write(str_to_bin(val))
        f.close()
        commands.append('-R {},{}'.format(port_to_address_map[line[0]], filename))

    print(' '.join(commands))
