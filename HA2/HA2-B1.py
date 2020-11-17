# Dining Cryptographers
# By Amanda Flote & Olivia Mattsson

def main():
    # Read a file with the content: 
    # SA, BA, DA, DB, M, b
    with open('HA2/DC.txt') as f:
        lines = f.read().splitlines()
        dataA, dataB, message, b = getInfo(lines)
        
        test = hex(int(str(dataA[0]), 16) ^ int(str(dataB[0]), 16) ^ int(str(message), 16))
        print(test)
        # If we want to broadcast our message
        if b==1:
            # Compute the broadcasted data:

            return
        # If we doesn't want to broadcast our message
        elif b==0:
            # XOR the shared secrets:
            xorsecrets = hex(int(str(dataA[0]), 16) ^ int(str(dataB[0]), 16))
            print("XOR: {0}".format(xorsecrets))
            return
        else:
            raise Exception("Wrong value of b.")
        return

    # XOR: hex(int("hexastring", 16) ^ int("hexastring", 16))

def getInfo(input):
    return input[:2], input[2:4], input[4], int(input[5])


if __name__ == '__main__':
    main()

