#!/usr/bin/env python3
#
#This program converts a number to another base.

import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        print('Converts a number to another base.')
        print('')
        print('baseChange.py [-b][-x][-o][-d] number')
        print('')
        print('\t-b    Converts number to binary')
        print('\t-x    Converts number to hexadecimal')
        print('\t-o    Converts number to octal')
        print('\t-d    Converts number to decimal')
        print('')
        print('If using something other than decimal, use the following prefixes:')
        print('\tBinary: 0b')
        print('\tHex:    0x')
        print('\tOct:    0o')
        print('\tIf no prefix is used, decimal base is assumed.')
        print('')
        print('EXAMPLES:')
        print('\tbaseChange.py -x 100')
        print('\tbaseChange.py -d 0b1001')
        return
        
    elif len(sys.argv) == 3:
        if not checkIfValid(sys.argv[2][2:],sys.argv[2][:2]):
            print('That is not a valid number for that base. Try again.')
            return
        
        if sys.argv[1] == '-b':
            if sys.argv[2][:2] == '0x':
                print(bin(int(sys.argv[2],16))[2:])
                return
            elif sys.argv[2][:2] == '0o':
                print(bin(int(sys.argv[2],8))[2:])
                return
            elif sys.argv[2][:2] == '0b':
                print(sys.argv[2][2:])
                return
            else:
                print(bin(int(sys.argv[2]))[2:])
                return
        elif sys.argv[1] == '-x':
            if sys.argv[2][:2] == '0b':
                print(hex(int(sys.argv[2],2)).upper()[2:])
                return
            elif sys.argv[2][:2] == '0o':
                print(hex(int(sys.argv[2],8)).upper()[2:])
                return
            elif sys.argv[2][:2] == '0x':
                print(sys.argv[2][2:].upper())
                return
            else:
                print(hex(int(sys.argv[2]))[2:].upper())
                return
        elif sys.argv[1] == '-o':
            if sys.argv[2][:2] == '0b':
                print(oct(int(sys.argv[2],2))[2:])
                return
            elif sys.argv[2][:2] == '0x':
                print(oct(int(sys.argv[2],16))[2:])
                return
            elif sys.argv[2][:2] == '0o':
                print(sys.argv[2][2:])
                return
            else:
                print(oct(int(sys.argv[2]))[2:])
        elif sys.argv[1] == '-d':
            if sys.argv[2][:2] == '0x':
                print(int(sys.argv[2],16))
                return
            elif sys.argv[2][:2] == '0o':
                print(int(sys.argv[2],8))
                return
            elif sys.argv[2][:2] == '0b':
                print(int(sys.argv[2],2))
                return
            else:
                print(sys.argv[2])
                return
        else:
            print('Usage: baseChange.py [-b][-x][-o][-d] number')
            print('Use --help for more information')
            return
            
    else:
        print('Usage: baseChange.py [-b][-x][-o][-d] number')
        print('Use --help for more information')
        return
    
def checkIfValid(s,base):
    if base == '0x':
        for i in s:
            if i not in ('1234567890abcdefABCDEF'):
                return False
        return True
    elif base == '0o':
        for i in s:
            if i not in ('01234567'):
                return False
        return True
    elif base == '0b':
        for i in s:
            if i not in ('01'):
                return False
        return True
    else:
        return (base + s).isnumeric()
        
    
        
        
        
if __name__ == "__main__":
    main()

















