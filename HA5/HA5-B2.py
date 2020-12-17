# Identity based encryption scheme
# By Olivia Mattsson and Amanda Flote
import hashlib

# Inputs:
identity = 'walter@crypto.sec'
p = '9240633d434a8b71a013b5b00513323f'
q = 'f870cfcd47e6d5a0598fc1eb7e999d1b'
encryptedBits = ['0b62a946b76845e44591e79a9fe1f8a2d44095fad9d3543a570f65a2168b5051',
'2bdd5d58fe150fc75ad2f6f0858f0df3128597b1e06bdde3cbeb7605f5b39dcd',
'7911234bca14066caf7831449a8dbdef32c7b24c53e948765c0e803da77353a3',
'7e9c90937d6eb21f93fd4cf37d3ee126e6eb5e600d05ae3a58816db60c3fb74b',
'5d4e9a468e76b863d3969d7f844752545eac0baabebdf10b42e9e679b5ce15a5',
'52f9c7c50a00cee060ce12012b7fadb094ea0d920ff4d3f0fc2c8a92afea8020',
'5d1717c2eebadd66a3192ce361e1ede546d96db9d287c722528d3f4932d8c640',
'19a3ebbdf8b31209200c24b76cc3735d7f12cdc1b544b80bc995f3bcb1836eda']

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
   
    