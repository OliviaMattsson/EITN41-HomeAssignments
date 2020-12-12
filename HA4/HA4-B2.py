# OTR
# By Amanda Flote & Olivia Mattsson

import hashlib, socket, random, math

sharedSecret = "eitn41 <3"
p = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF",16)
g = 2



def main():
    # format(1337, 'x') - to hexastring
    
    # COPIED FROM TEST-CLIENT.PY
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    soc.connect(("eitn41.eit.lth.se", 1337))

   
    def agreement():
    # Ta kod från test-client för sockets osv. 
        g_x1 = soc.recv(4096).decode('utf8').strip()
        print ('g**x1:', g_x1)
    # interpret as a number
        g_x1 = int(g_x1, 16)
    # generate g**x2, x2 shall be a random number
        x2 = random.randrange(2,p)
    # calculate g**x2 mod p
        g_x2 = pow(g, x2, p)
    # convert to hex-string
        g_x2_str = format(g_x2, 'x').encode('utf8')
    # send it
        soc.send(g_x2_str)
    # read the ack/nak. This should yield a nak due to x2 being 0
        print ('\nsent g_x2:', soc.recv(4096).decode('utf8').strip())
    #Agree on shared key
        sharedKey = pow(g_x1, x2, p)
        sharedKey = I20SP(sharedKey, (sharedKey.bit_length() + 7) // 8)
        return sharedKey, x2

    sharedKey,BobExp = agreement()
    gen2,BobExp2 = agreement()
    gen2 = int.from_bytes(gen2, 'big')
    gen3,BobExp3 = agreement()
    gen3 = int.from_bytes(gen3, 'big')
    P,Q = calculatePQ(g, gen2, gen3, sharedKey, p)

    Pa  = int(soc.recv(4096).decode('utf8').strip(),16)
    soc.send(str(P).encode('utf8'))
    print ('\nsent P:', soc.recv(4096).decode('utf8').strip())

    Q_a  = soc.recv(4096).decode('utf8').strip()
    soc.send(str(Q).encode('utf8'))
    print ('\nsent Q:', soc.recv(4096).decode('utf8').strip())

    
    
    # Inverse Qb in modulo p! Equlidean algorithm
    Q_b = inverse(Q)
    Q_c = int(Q_a,16) * Q_b
    # Qb should be in Z_p* and Q_a * Q_b^-1 should also be in Z_p* and BobExp3 same.
    Rb = pow(Q_c, BobExp3, p) 
    Rb = format(Rb, 'x').encode('utf8')
    Ra = int(soc.recv(4096).decode('utf8').strip(),16)
    soc.send(Rb)
    print ('\nsent Rb:', soc.recv(4096).decode('utf8').strip())
    print ('\nsent authentication:', soc.recv(4096).decode('utf8').strip())
    Rab = pow(Ra, BobExp3, p)
    Pb_inv = inverse(P)
    print('ACK', Rab == Pa * Pb_inv % p)
    print(Rab)
    print(Pa * Pb_inv % p)
    """
    #Send message - kanske rätt kanske inte
    message = "Hej"
    message = I20SP(message, )
    encryptedMessage = bytes(a ^ b for a, b in zip(message,sharedKey))
    soc.send(encryptedMessage.encode('utf8'))
    receivedMessage = soc.recv(4096).decode('utf8').strip()
    receivedMessage = receivedMessage.encode("utf8")
    receivedMessage = int(receivedMessage, 16)
    receivedMessage = (receivedMessage ^ int(str(sharedKey), 16))
    receivedMessage = receivedMessage.to_bytes((receivedMessage.bit_length() + 7) // 8, 'big')
    print ('\nsent message:', receivedMessage)
    print ('\nreceived back:', soc.recv(4096).decode('utf8').strip())"""

def calculatePQ(gen1, gen2, gen3, sharedKey, p):
    b = random.randrange(2,p)
    y = sha_hash(sharedKey + sharedSecret.encode('utf8'))
    print("y :" + y) 
    P= pow(gen3, b, p)
    Q= pow(gen1, b, p) * pow(gen2, int(y,16), p)
    return P,Q

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


def inverse(val):
    # We need to find x so that x*val % p is equivalent to 1, using the
    # extended Euclidean algorithm:
    y, x = euc_alg(val, p)
    if y == 1:
        print(x%p)
        return x % p


def euc_alg(val, p):
    # Extended Euclidean algorithm, inspiration from wikipedia and other source: 
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    # http://anh.cs.luc.edu/331/notes/xgcd.pdf , page 2
    t, newt = 1, 0
    r, newr = 0, 1
    while p != 0:
        quotient = val // p
        val, p = p, val % p
        t, newt = newt, t - (quotient * newt)
        r, newr = newr, r - (quotient * newr)
    if t < 0:
        t = t + p
    return  val, t

   


# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    return h

if __name__ == '__main__':
    main()
