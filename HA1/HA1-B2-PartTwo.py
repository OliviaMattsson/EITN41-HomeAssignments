# PART TWO - Full Node
# Implement a program that takes an integer index i, another integer index j, and a set of leaves, 
# (l(0), l(1), l(2), . . . , l(n − 1)), in a Merkle tree. 
# The leaves are given as hexadecimal strings as input, but should be interpreted as byte arrays. 
# The input is summarized in a file, starting with the integer index i, the integer index j, 
# and then followed by the leaves, one input on each line. Your program should provide:

# 1. The Merkle path for leaf l(i), starting with the sibling of l(i).
# 2. The Merkle path node at a given depth j (this will be used in the assessment). 
# 3. The resulting Merkle root (this will be used in the assessment).

import array
import hashlib
import binascii
import math



def main():
    with open('leaves5.txt') as f:
        lines = f.read().splitlines()

        # Retrieves the indexes i, j, and the leaves
        i = int(lines[0])
        j = int(lines[1])
        leaves = lines[2:]
        path = []
        (root, pathList) = createtree(leaves, i, path)
        print(pathList[-j] + root[0])
    return

def createtree(leaves, i, path):
    newPath = path
    nextiVal = i
    nextlevel = []
    if len(leaves) % 2 != 0:
        leaves += leaves[-1:]
    for x in range(0, len(leaves), 2):
        newNode = leaves[x] + leaves[x+1]
        newNode = sha_hash(hexa_to_byte(newNode))
        nextlevel.append(newNode)
        if x == i:
            # The new path node is on the right
            newPath.append("R" + str(leaves[x+1]))
            nextiVal = len(nextlevel)-1
        elif (x+1) == i:
            # The new path node is on the left
            newPath.append("L" + str(leaves[x]))
            nextiVal = len(nextlevel)-1
        
        
    if len(nextlevel) == 1:
        print(newPath)
        return nextlevel, newPath
    else:    
        return createtree(nextlevel, nextiVal, newPath)

#Hexdec string to byte array
def hexa_to_byte(inputVal):
    return bytearray.fromhex(inputVal)

# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    return h

if __name__ == '__main__':
    main()


