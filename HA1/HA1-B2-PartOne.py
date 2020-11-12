# PART ONE - SPV NODE
# By Olivia Mattsson and Amanda Flote

import hashlib



def main():
    with open('HA1/SPVnode.txt') as f:
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

