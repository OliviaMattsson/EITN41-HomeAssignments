# OTR
# By Amanda Flote & Olivia Mattsson

import hashlib, socket, random, math





def main():
    #Create Rb - här får vi too big int
    
    Qa_256 = I20SP(270, int(math.log(270, 256)+1)) # 256^1 + 3*256^0 , should be x00 x01 x03
    print("Qa: {0}".format(Qa_256))
    Q_256 = I20SP(16777216, int(math.log(16777216, 256)+1)) # 256 ^ 3 , should be x01 x00 x00 x00
    print("Q_256: {0}".format(Q_256))
    # Rb = pow(int.from_bytes(Qa_256, 'big') * pow(Q_256, -1), 2, 2) # TODO




# I20SP function
def I20SP (x, xLen):
    xLen = math.ceil(xLen)
    # If x >= 256^xLen, output "integer too large" and stop.
    if x >= 256**xLen:
        print("Integer too large")
        return
    # Make a representation of X in base 256:
    X = bytearray(xLen)
    for i in range(0,xLen-1):
        # For each value on i, we want to find out what we need to multiply 256^(xLen-i) with to get the part
        X[i] = x // (256**(xLen-1-i))
        x = x % (256**(xLen-1-i))
    X[xLen - 1] = x
    # Return the base 256 X value:
    return X


if __name__ == '__main__':
    main()
