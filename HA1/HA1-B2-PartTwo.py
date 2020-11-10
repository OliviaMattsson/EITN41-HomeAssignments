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



def main():
    with open('HA1/FullNode.txt') as f:
        lines = f.read().splitlines()
        i = lines[0]
        j = lines[1]
        leaves = lines[2:]
        print(i, j, leaves)
        
        test = hexa_to_byte("")
        sha1 = hexa_to_byte(sha_hash(test))
        sha2 = hexa_to_byte(sha_hash(test))
        sha3 = hexa_to_byte(sha_hash(test))
        sha4 = hexa_to_byte(sha_hash(test))
        
        level2l = hexa_to_byte(sha_hash(sha1 + sha2))
        level2r = hexa_to_byte(sha_hash(sha3 + sha4))

        level1 =sha_hash(level2l +level2r)

        print(level1)
    return

#Hexdec string to byte array
def hexa_to_byte(inputVal):
    val = bytearray.fromhex(inputVal)
    
    print("modified hexadec: " + inputVal)
    #val = binascii.unhexlify(inputVal)
    print("Hexa to byte array: " + str(val))
    return val


# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    print("Sha hash: " + h)
    return h
    








if __name__ == '__main__':
    main()


