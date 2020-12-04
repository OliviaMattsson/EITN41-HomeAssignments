import hashlib
from math import ceil
import random


hLen = 20
k = 128


def I20SP (x, xLen):
    if x >= 256**xLen:
        return "integer too large"
    return (hex(x)[2:].zfill(2*xLen))



def MGF1(mgfSeed, maskLen):
    if maskLen >= 2**32 * hLen:
        return "mask too long"
    T = ""
    for i in range(0, int(ceil(maskLen / hLen))):
        C = I20SP (i, 4)
        T = T + hashlib.sha1(bytearray.fromhex(mgfSeed + C)).hexdigest()
                
    return T[:2*maskLen]


def OAEP_encode(M, seed):
    if len(M) > (k - 2 * hLen - 2):
        return "message too long"
    L = ""
    lHash = hashlib.sha1(bytearray(L.encode())).hexdigest()
    PS = "".zfill(((k - int(len(M)/2) - 2*hLen) - 2)*2)
    print("PS: " + PS)
    DB = lHash + PS + "01" + M 
    print("DB: " + DB)
    random_octet = str(bytearray(random.getrandbits(8) for _ in range(hLen)))
    dbMask = MGF1(seed, k - hLen - 1)
    print("dbMask: " + dbMask)
    maskedDB = hex(int(DB, 16) ^ int(dbMask, 16))[2:]
    print("maskedDB: " + maskedDB)
    seedMask = MGF1(maskedDB, hLen)
    print("seedMask: " + seedMask)
    maskedSeed = hex(int(seed, 16) ^ int(seedMask, 16))[2:]
    print("maskedSeed: " + maskedSeed)
    EM = "00" + maskedSeed + maskedDB
    return EM

def OAEP_decode (EM):
    L = ""
    lHash = hashlib.sha1(bytearray(L.encode())).hexdigest()
   
    Y = EM[:2]
    maskedSeed = EM[2:2 * hLen + 2]
    maskedDB = EM[2 * hLen + 2:]
    seedMask = MGF1(maskedDB, hLen)
   
    seed = hex(int(maskedSeed, 16) ^ int(seedMask, 16))[2:]
    dbMask = MGF1(seed, k - hLen - 1)
    DB = hex(int(maskedDB, 16) ^ int(dbMask, 16))[2:]
   
    lPrimeHash = DB[:hLen]
    PS = DB[hLen * 2: hLen * 2 + DB[hLen * 2:].find("01") + 2]
    M = DB[hLen * 2 + len(PS):]

    return M


    
if __name__ == '__main__':
  
    mgfSeed = "d9918d2cd546940c8b3beccd09c5e1d58c72b4998c7f52a5f267"
    maskLen = 26

    M = "c107782954829b34dc531c14b40e9ea482578f988b719497aa0687"
    seed = "1e652ec152d0bfcd65190ffc604c0933d0423381"
    
    
    EM = "00581bc2381cf79218566065eb1def452262df368e129de319b5c2bb66e84df6be244fc653a9468c6aafbe715fe366526e9596c452cdf7a42ddcec8d8005724dc7d9450b769aa0fe6f58e8949e503294de3106a7a3b0254eac2b94d245421e610ca70466137c29e7ff5ccd41dda83a44457ea3c820d0f360599833d34ec82e3b"
  
    print("MGF1 output: " + MGF1(mgfSeed, maskLen))
    print("<==============================================================>")
    print("OAEP encode output: " + OAEP_encode(M, seed)) 
    print("<==============================================================>")
    print("OAEP decode output: " + OAEP_decode(EM)) 