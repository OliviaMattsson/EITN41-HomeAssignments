# OAEP for RSA
# By Amanda Flote & Olivia Mattsson
import math
import hashlib


def main():
    # Read a file with the content: 
    with open('HA4/testfiles/b1.txt') as f:
        lines = f.read().splitlines()
    

# Mask Genereation Function
def MGF1(mgfSeed, maskLen):
    # Since we use SHA1:
    hLen = 40
    # If maskLen > 2^32 hLen, output "mask too long" and stop.
    if maskLen > 2**32 * hLen:
        print("Mask too long")
        return
    #  Let T be the empty octet string (byte string)
    T = ""
    # For counter from 0 to \ceil (maskLen / hLen) - 1:
    for i in range(math.ceil(maskLen/hLen) - 1):
        # Convert counter to an octet string C of length 4 octets:
        C = I2OSP (i, 4)

        # Concatenate the hash of the seed mgfSeed and C to the octet string T:
        T += sha_hash(mgfSeed + C) 
    return T

# IOSP function
def I2OSP(x, xLen):

    # If x >= 256^xLen, output "integer too large" and stop.
    if x > 256**xLen:
        print("Integer too large")
        return
    # Make a representation of X in base 256: 
    X = ""
    for i in range(xLen):
        X += x * 256**xLen
    # Return the base 256 X value:
    return X

# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    return h

if __name__ == '__main__':
    main()
