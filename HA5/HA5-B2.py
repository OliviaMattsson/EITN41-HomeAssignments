# Identity based encryption scheme
# By Olivia Mattsson and Amanda Flote
import hashlib

# Inputs:
identity = 'craig@crypto.sec'
p = '9240633d434a8b71a013b5b00513323f'
q = 'f870cfcd47e6d5a0598fc1eb7e999d1b'

encryptedBits = ['78c4125df8a0a0201ad8443349a50dfe8da7781865190f0d6c42c414c9b5178a',
'3bb1377035c5fff518b1b7c9fe2c4a072f33059b549e85390e80f55a75a215c6',
'8dc799a9b1eedb344ec7b5f1ad85b5b655cb0edbc4f903b242f45e5540eb62ed',
'86d096b16e9c4ddd3b9dbe8a0e8405676d0fe03a4bca55e1cfb590654d3bed11',
'1c43ea858ad3b379a7935118df21abbf6484d95c2782ce8f542033bf5e0aa75f',
'612be2f70240c427799fcba3b70b6fc01dea8385ec86347bdbe1e857f6f74af7',
'4796d276924394d29907798cfe9668da086126cbcd5d63ccb1c54e117a4ec85e',
'5205e0c007fff45f6c1f614bf3346b11b98b428f21aa854ba368e49f7dfc63d2']

def main():
    M= int(p,16)*int(q,16)
    hashedEmail = sha_hash(identity.encode('utf8'), M)
    j = jacobi(int.from_bytes(hashedEmail,byteorder='big'),M)
    foundHash = True
    if(j== 1):
        foundHash = False
    while(foundHash):
        hashedEmail = sha_hash(hashedEmail,M)
        j = jacobi(int.from_bytes(hashedEmail,byteorder='big'),M) 
        if(j == 1):
            foundHash = False
            
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
    