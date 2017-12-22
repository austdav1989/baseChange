# baseChange

Converts a number to another base.

baseChange.py [-b][-x][-o][-d] number

-b    Converts number to binary

-x    Converts number to hexadecimal

-o    Converts number to octal

-d    Converts number to decimal


If using something other than decimal, use the following prefixes:

Binary: 0b

Hex:    0x

Oct:    0o

If no prefix is used, decimal base is assumed.

EXAMPLES:

baseChange.py -x 100

baseChange.py -d 0b1001