'''This script prints the alphabet in lowercase'''
small_letters = map(chr, range(ord('a'), ord('z')+1))
az = small_letters[0:(ord('z')-ord('a')+1)]
print("".join(small_letters))
'''join allows to print without spaces between characters'''
''' chr(i) returns a string of one character whose ASCII code is the integer i. For example, chr(97) returns the string 'a'.'''
