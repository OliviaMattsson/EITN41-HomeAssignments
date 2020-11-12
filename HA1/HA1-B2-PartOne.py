# PART ONE - SPV NODE
# Implement a program that takes a file with a leaf node L, given as a hexadecimal string, and a Merkle path as input, with each node in the path on a separate line. 
# The 2t-byte strings should be interpreted as t-byte byte arrays. The Merkle path nodes are given in the order of highest depth first, i.e., the leaf node sibling. 
# By convention, the root node is at depth 0 and the leaves are at depth ⌈log2 n⌉, where n is the number of leaves. 
# Each string representing nodes in the Merkle path is preceded by the letter ’L’ or ’R’, indicating if the sibling node in the path is a Left or Right node. 
# The program should output the Merkle root as a hexadecimal string. Use SHA-1 as hash function throughout the tree and merge nodes using concatenation of SHA-1 results (byte arrays).

import array
import hashlib
import binascii



def main():
    with open('SPVnode.txt') as f:
        lines = f.read().splitlines()
        # Retrieves our start value - first hash with first leaf
        firstValue = lines[0] + lines[1][1:]
        # Converts to byte array
        firstValue= hexa_to_byte(firstValue)
        # Hashes the value
        firstValue = sha_hash(firstValue)
        # Appends the rest of the leaves
        print(appendSHA(firstValue, lines[2:]))


def appendSHA(startValue, lines):
    lastValue = startValue
    for line in lines: 
        # Depending on if the node is left or right, append the lastValue on the correct side
        if (line[0:1]== 'L'):
            line = line[1:] + lastValue
        else:
            line = lastValue + line[1:]
        # Converts to correct format and hashes the string
        line = hexa_to_byte(line)
        line = sha_hash(line)
        # Puts the computed value in our lastValue to continue the loop
        lastValue= line
    return lastValue

#Hexdec string to byte array
def hexa_to_byte(inputVal):
    return bytearray.fromhex(inputVal)


# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    return h

if __name__ == '__main__':
    main()

