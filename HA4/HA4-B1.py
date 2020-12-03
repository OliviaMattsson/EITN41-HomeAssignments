# OAEP for RSA
# By Amanda Flote & Olivia Mattsson
import math
import hashlib

# Länk till RFC: https://tools.ietf.org/html/rfc8017

def main():
    # Read a file with the content: 
    with open('HA4/testfiles/b1.txt') as f:
        lines = f.read().splitlines()
    
    # RSAES-OAEP Scheme

    # RSAEP primitive (Section 5.1.1)
    c = RSAEP(pubKey, m)
    # RSADP primitive (Section 5.1.2)
    message = RSADP(privKey, c)
    # EME-OAEP encoding method (Section 7.1)
        # EME-OAEP encoding: Step 2 in 7.1.1
        
        # EME-OAEP decoding: Step 3 in 7.1.2



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

# RSAEP primitive (Section 5.1.1)
def RSAEP(pubKey, m):
    n, e = pubKey
    c = ""
    return c

# RSADP primitive (Section 5.1.2)
def RSADP(privKey, c):
    n, d, quint, c = privKey
    m = ""
    return m


# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    return h

if __name__ == '__main__':
    main()
