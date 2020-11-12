# PART TWO - Full Node
# By Olivia Mattsson and Amanda Flote

import hashlib



def main():
    with open('HA1/leaves9.txt') as f:
        lines = f.read().splitlines()

        # Retrieves the indexes i, j, and the leaves
        i = int(lines[0])
        j = int(lines[1])
        leaves = lines[2:]
        path = []
        # Retrieves the root and the list of path nodes from createtree()
        (root, pathList) = createtree(leaves, i, path)
        print(pathList[-j] + root[0])
    return

def createtree(leaves, i, path):
    # Copies the list of nodes hashed with in the path and the value of i to look for
    newPath = path
    nextiVal = i
    # Creates a new list for the current level we are at
    nextlevel = []
    # If there is an uneven amount of nodes, we add the last node to the list
    if len(leaves) % 2 != 0:
        leaves += leaves[-1:]
    # Iterates over the nodes on the current level
    for x in range(0, len(leaves), 2):
        # Creates a new node, hash it and add to the new level
        newNode = leaves[x] + leaves[x+1]
        newNode = sha_hash(hexa_to_byte(newNode))
        nextlevel.append(newNode)

        # Two methods if our i value was found - adds the neighbour to the list of path nodes
        if x == i:
            # The new path node is on the right
            newPath.append("R" + str(leaves[x+1]))
            # The new i value to look for in the next loop
            nextiVal = len(nextlevel)-1
        elif (x+1) == i:
            # The new path node is on the left
            newPath.append("L" + str(leaves[x]))
            # The new i value to look for in the next loop
            nextiVal = len(nextlevel)-1
        
    # If we are in the top root, we stop the function calls and return the list
    # of paths and the root level node
    if len(nextlevel) == 1:
        return nextlevel, newPath
    # If we are not on the root level, we call the function again    
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


