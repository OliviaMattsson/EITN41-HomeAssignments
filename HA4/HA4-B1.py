# OAEP for RSA
# By Amanda Flote & Olivia Mattsson
import math
import hashlib

# Länk till RFC: https://tools.ietf.org/html/rfc8017
hLen = 20

def main():
    m = "c107782954829b34dc531c14b40e9ea482578f988b719497aa0687"
    seed = "1e652ec152d0bfcd65190ffc604c0933d0423381"
    encMessage = "0063b462be5e84d382c86eb6725f70e59cd12c0060f9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51efc06d40d25f96bd0f4c5d88f32c7d33dbc20f8a528b77f0c16a7b4dcdd8f"
    # RSAES-OAEP Scheme
    res = MGF1('9b4bdfb2c796f1c16d0c0772a5848b67457e87891dbc8214', 21)
    print("MGF1: {0}".format(res))
    print("-------------------------")

    # EME-OAEP encoding: Step 2 in 7.1.1
    c = OAEPencode(seed, m)
    print("Encrypted message: " + c)
    print("-------------------------")
    # EME-OAEP decoding: Step 3 in 7.1.2
    decrypted = RSADP(encMessage)
    print("Decrypted message: " + decrypted)
            
    

def OAEPencode(seed, message):
    lHash = hashlib.sha1(bytearray("".encode())).hexdigest()
    mLen = int(len(message)/2)
    k = 128
    PS = (k - mLen - 2*hLen) - 2
    padding = "".zfill((PS*2))
    DB = lHash + padding + "01" + message
    dbMask = MGF1(seed, (k - hLen - 1))
    maskedDB = hex(int(DB,16) ^ int(dbMask, 16))[2:]
    seedMask = MGF1(maskedDB, hLen).lstrip("0x")
    maskedSeed = hex(int(seed,16) ^ int(seedMask, 16))[2:]
    encMessage = "00" + maskedSeed + maskedDB
    return encMessage

def OAEPdecode():
    # TODO
    return


# Mask Genereation Function
def MGF1(mgfSeed, maskLen):
    # If maskLen > 2^32 hLen, output "mask too long" and stop.
    if maskLen > (2**32) * hLen:
        print("Mask too long")
        return
    #  Let T be the empty octet string (byte string)
    T = ""
    # For counter from 0 to \ceil (maskLen / hLen) - 1:
    for i in range(0,math.ceil(maskLen/hLen)):
        # Convert counter to an octet string C of length 4 octets:
        C = I2OSP (i, 4)
        
        # Concatenate the hash of the seed mgfSeed and C to the octet string T:
        T += sha_hash(mgfSeed + C) 
    
    # Output the leading maskLen octets of T as the octet string mask.
    
    return T[:2*maskLen]

# I20SP function
def I2OSP(x, xLen):

    # If x >= 256^xLen, output "integer too large" and stop.
    if x >= 256**xLen:
        print("Integer too large")
        return
    # Make a representation of X in base 256: 
    X = ""
    for i in range(1,xLen+1):
        if i == xLen:
            res = x
        elif (x / (256**(xLen-i))) > 1:
            res = int(x - math.floor(x / (256**(xLen-i))))
            x = x - res        
        else:
            res = "0"
        X += str(res)
    # Return the base 256 X value:
    return (X.zfill(2*xLen))


# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(bytearray.fromhex(inputVal)).hexdigest()
    return h

if __name__ == '__main__':
    main()
