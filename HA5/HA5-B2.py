# Identity based encryption scheme
# By Olivia Mattsson and Amanda Flote
import hashlib

# Inputs:
identity = 'craig@crypto.sec'
p = '9240633d434a8b71a013b5b00513323f'
q = 'f870cfcd47e6d5a0598fc1eb7e999d1b'
# Output 220 mail: walter@crypto.sec
#encryptedBits = ['0b62a946b76845e44591e79a9fe1f8a2d44095fad9d3543a570f65a2168b5051','2bdd5d58fe150fc75ad2f6f0858f0df3128597b1e06bdde3cbeb7605f5b39dcd','7911234bca14066caf7831449a8dbdef32c7b24c53e948765c0e803da77353a3','7e9c90937d6eb21f93fd4cf37d3ee126e6eb5e600d05ae3a58816db60c3fb74b','5d4e9a468e76b863d3969d7f844752545eac0baabebdf10b42e9e679b5ce15a5','52f9c7c50a00cee060ce12012b7fadb094ea0d920ff4d3f0fc2c8a92afea8020','5d1717c2eebadd66a3192ce361e1ede546d96db9d287c722528d3f4932d8c640','19a3ebbdf8b31209200c24b76cc3735d7f12cdc1b544b80bc995f3bcb1836eda']

#Test output 42 mail: walterwhite@crypto.sec
#encryptedBits =['2f2aa07cfb07c64be95586cfc394ebf26c2f383f90ce1d494dde9b2a3728ae9b','63ed324439c0f6b823d4828982a1bbe5c34e66d985f55792028acd2e207daa4f','85bb7964196bf6cce070a5e8f30bc822018a7ad70690b97814374c54fddf8e4b','30fbcc37643cc433d42581f784e3a0648c91c9f46b5671b71f8cc65d2737da5c','5a732f73fb288d2c90f537a831c18250af720071b6a7fac88a5de32b0df67c53','504d6be8542e546dfbd78a7ac470fab7f35ea98f2aff42c890f6146ae4fe11d6','10956aff2a90c54001e85be12cb2fa07c0029c608a51c4c804300b70a47c33bf','461aa66ef153649d69b9e2c699418a7f8f75af3f3172dbc175311d57aeb0fd12']

#Riktigt quiz mail: craig@crypto.sec kolla med fred om vi får samma output
encryptedBits =['7a467d8e4c1895947664b67b5a2cc1b8fba212b29e2f55c6dc201f6a47112763','75ab77f877d66cc5fe64d3ebf76d5c633b9c6a5ed904824a6a3ed897225116cb','753b0a35978ba3638e9ef9965779316234748db6323c86ecd95e89b420bc3c56','09c5c347811bdc8d893128b0a6a0e14815e5b0aa320c34dd8364f8d1cf8e7d09','5a3674a974783eb795bcae3b5589d1fe20adf164fbeec5818632991792b1999d','5834692bc1de2f9f350fa4712043ff0c9b3dfdc36de5dbd7b2a0afb41df90832','4e384060c535327d1359734f2e5a69a7c315547832b9104b4dc69c2fb805c4e5','5702fcacce8d1db61304ce4eda30ff9045c12c7965fe4ee6209883ce98a84acb']
def main():
    M= int(p,16)*int(q,16)
    hashedEmail = sha_hash(identity.encode('utf8'), M)
    j = jacobi(int.from_bytes(hashedEmail,byteorder='big'),M)
    foundHash = True
    attempt = 0
    if(j== 1):
        foundHash = False
    #hashedEmail = sha_hash(hashedEmail,M)
    while(foundHash):
        print("I while")
        attempt += 1
        hashedEmail = sha_hash(hashedEmail,M)
        j = jacobi(int.from_bytes(hashedEmail,byteorder='big'),M) 
        if(j == 1):
            print("här")
            foundHash = False
            
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
    