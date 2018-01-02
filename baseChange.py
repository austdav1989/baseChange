#!/usr/bin/env python
#
#This program converts a number to another base.

import sys

def main():
    if len(sys.argv) == 3:
        if not checkIfValid(sys.argv[2][2:],sys.argv[2][:2]):
            print('That is not a valid number for that base. Try again.')
            return
        
        printBase(sys.argv[1],sys.argv[2])
        
    else:
        print('Usage: baseChange.py [-b][-x][-o][-d] number')
        print('Use --help for more information')
        return
    
def checkIfValid(s,base): #Parses number to check if valid
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
    
def convertBase(num): #converts base to base 10 for simplicity
    if num[:2] == '0x':
        return int(num[2:],16)
    elif num[:2] == '0o':
        return int(num[2:],8)
    elif num[:2] == '0b':
        return int(num[2:],2)
    else: 
        return num
    
def printBase(arg,num): #Function to print number in new base
    if arg == '-b':
        print(bin(int(convertBase(num)))[2:])
        return
    elif arg == '-x':
        print(hex(int(convertBase(num)))[2:].upper())
        return
    elif arg == '-o':
        print(oct(int(convertBase(num)))[2:])
        return
    elif arg == '-d':
        print(int(convertBase(num))[2:])
        return
    elif arg == '--help':
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
    else:
        print('Usage: baseChange.py [-b][-x][-o][-d] number')
        print('Use --help for more information')
        return
if __name__ == "__main__":
    main()