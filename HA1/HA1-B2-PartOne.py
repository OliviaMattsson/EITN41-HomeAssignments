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
    return









if __name__ == '__main__':
    main()

