import random as r
import numpy as np

letterDict = {0: ' ', 1: 'a',
              2: 'b', 3: 'c',
              4: 'd', 5: 'e',
              6: 'f', 7: 'g',
              8: 'h', 9: 'i',
              10: 'j', 11: 'k',
              12: 'l', 13: 'm',
              14: 'n', 15: 'o',
              16: 'p', 17: 'q',
              18: 'r', 19: 's',
              20: 't', 21: 'u',
              22: 'v', 23: 'w',
              24: 'x', 25: 'y',
              26: 'z', 27: 'A',
              28: 'B', 29: 'C',
              30: 'D', 31: 'E',
              32: 'F', 33: 'G',
              34: 'H', 35: 'I',
              36: 'J', 37: 'K',
              38: 'L', 39: 'M',
              40: 'N', 41: 'O',
              42: 'P', 43: 'Q',
              44: 'R', 45: 'S',
              46: 'T', 47: 'U',
              48: 'V', 49: 'W',
              50: 'X', 51: 'Y',
              52: 'Z', 53: '.',
              54: ',', 55: '\'',
              56: ';', 57: '!',
              58: '(', 59: ')',
              60: '\"', 61: '=',
              62: '@', 63: '#',
              64: '$', 65: '%',
              66: '^', 67: '&',
              68: '*', 69: '_',
              70: '<', 71: '>',
              72: '?', 73: ':',
              74: '~', 75: '`',
              76: '-', 78: '\\',
              79: '/', 80: '1',
              81: '2', 82: '3',
              83: '4', 84: '5',
              85: '6', 86: '7',
              87: '8', 88: '9',
              89: '0', 90: '|',
              91: '+'}

x = input('')
encodingMatrix = []
encodedMessMatrix = []
decodedMessage = []

for i in range(3):
    encodingMatrix.append(r.randint(1, 100))

print(encodingMatrix)

for i in x:
    for j in letterDict:
        if i == letterDict[j]:
            encodedMessMatrix.append(j)
        else:
            continue


print('Starting: ', encodedMessMatrix)

for i in encodedMessMatrix:
    
    encodedMessMatrix.append(encodedMessMatrix.pop(0)*2)

for i in encodedMessMatrix:
    
    encodedMessMatrix.append(encodedMessMatrix.pop(0) // 2)
print('Decoded: ', encodedMessMatrix)


for i in encodedMessMatrix:
    for j in letterDict:
        if i == j:
            decodedMessage.append(letterDict[j])
        else:
            continue

output = ''

for i in decodedMessage:
    output = output + i
print(output)
