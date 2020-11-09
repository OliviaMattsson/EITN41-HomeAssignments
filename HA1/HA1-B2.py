# PART ONE
# Implement the Luhn algorithm in your favorite language. 
# You will be given a list of card numbers with one digit censored with an “X”. 
# Use your implementation to find the censored digit in order for the card number to be valid. 
# You will be given a list of card numbers, one per line. 
# The answer is the concatenation of all censored digits, in order according to the list.
# The program should output the Merkle root as a hexadecimal string. 
# Use SHA-1 as hash function throughout the tree and merge nodes using concatenation of SHA-1 results (byte arrays).

# PART TWO
# Implement a program that takes an integer index i, another integer index j, and a set of leaves, 
# (l(0), l(1), l(2), . . . , l(n − 1)), in a Merkle tree. 
# The leaves are given as hexadecimal strings as input, but should be interpreted as byte arrays. 
# The input is summarized in a file, starting with the integer index i, the integer index j, 
# and then followed by the leaves, one input on each line. Your program should provide:

# 1. The Merkle path for leaf l(i), starting with the sibling of l(i).
# 2. The Merkle path node at a given depth j (this will be used in the assessment). 
# 3. The resulting Merkle root (this will be used in the assessment).
