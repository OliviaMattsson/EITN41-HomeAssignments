# Dining Cryptographers
# By Amanda Flote & Olivia Mattsson

def main():
    # Read a file with the content: 
    # SA, BA, DA, DB, M, b
    with open('HA2/testquizB1.txt') as f:
        lines = f.read().splitlines()
        secrets, data, message, b = getInfo(lines)
        # Compute the broadcasted data, which is SA XOR SB:
        XORdata = hex(int(str(secrets[0]), 16) ^ int(str(secrets[1]), 16))

        # If we want to broadcast our message, we XOR the secrets with our message:
        if b==1:
            XORdata = hex(int(XORdata,16) ^ int(str(message), 16))

        # If we don't want to broadcast our message, we XOR with the received data: 
        elif b==0:
            # XOR the sent data from the other sources:
            xorsecrets = hex(int(str(data[0]), 16) ^ int(str(data[1]), 16))
            # XOR our computed message with the received ones:
            xormessage = hex(int(XORdata, 16) ^ int(xorsecrets, 16))
        else:
            raise Exception("Wrong value of b.")
        
        # Clean up the broadcasted data
        XORdata = stripContent(XORdata)
        xormessage = stripContent(xormessage)
        print(XORdata + xormessage)
        return

def stripContent(input):
    val = input.lstrip('0x')
    while len(val) != 4:
        val = '0' + val
    return val.upper()

def getInfo(input):
    return input[:2], input[2:4], input[4], int(input[5])


if __name__ == '__main__':
    main()

