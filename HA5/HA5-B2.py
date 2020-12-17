# Identity based encryption scheme
# By Olivia Mattsson and Amanda Flote
import hashlib

# Inputs:
identity = 'wendy@crypto.sec'
p = '9240633d434a8b71a013b5b00513323f'
q = 'f870cfcd47e6d5a0598fc1eb7e999d1b'
encryptedBits = ['7a3de06528072d38fccd30c52ebae6536b0fa6d86459fc00157fae085aac91c8',
'586af7c3e0a10f41672b55120a21b8962b1467128ebb4a27780c36197ba1f827',
'4f75cf2ed24ad656643c4778b33f08a14cc88380c79c93a20979c68030c5fe9c',
'52cebec5b8e276560649507a641094c0018ef010e809acb256604f280ed46694',
'231519968e4585b410e4840e2e0b3a442e69679e765272711c9639d53e3017fe',
'6e72f5b2cde9e03c9431e6685cfa62f4254f6fe8d07b2d3b196fbab44aa99164',
'396b1effbb8f05a15d82c9424737588d7bdd2f8b87acae5c626c66822bbc5b4b',
'093485f019dda827ca54df573918fcb9eeb51734772aa85bd76028661cb5794a']

def main():
    M= int(p,16)*int(q,16)
    hashedEmail = sha_hash(identity.encode('utf8'), M)
    foundHash = False
    while(not foundHash):
        hashedEmail = sha_hash(hashedEmail,M)
        j = jacobi(int.from_bytes(hashedEmail,byteorder='big'),M) 
        if(j == 1):
            foundHash = True
    r= calculateRoot(int.from_bytes(hashedEmail,byteorder= 'big'), M)
    message = decrypt(r, encryptedBits, M)
    print(message)
    return int(message,2), hex(r).lstrip('0x')

# Using Cocks encryption scheme - PKG
def calculateRoot(a, M):
    r = pow(a, (M+5-(int(p,16)+int(q,16)))//8, M)
    return r

#Decryption:
def decrypt(r, m, M):
    l = ""
    for bit in m:
        j = jacobi(int(bit,16)+ 2*r, M)
        if (j<0):
            l+= '0'
        else:
            l+= '1'
    return l 
    
# Taken from assignment page: 
def jacobi (a, m):
    j = 1
    a %= m
    while a:
        t = 0
        while not a & 1:
            a = a >> 1
            t += 1
        if t & 1 and m % 8 in (3, 5):
            j = -j
        if (a % 4 == m % 4 == 3):
            j = -j
        a, m = m % a, a
    return j if m == 1 else 0


def sha_hash(email, M):
    h = hashlib.sha1(email).digest()
    return h
    


if __name__ == '__main__':
    m,r = main() 
    print('message: {0}'.format(m))
    print('root: {0}'.format(r))
    