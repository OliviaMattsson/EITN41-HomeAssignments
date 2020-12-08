# OTR
# By Amanda Flote & Olivia Mattsson

import hashlib
import socket
import random

sharedSecret = "eitn41 <3"




def main():
    # Read a file with the content: 
    with open('HA4/testfiles/p.txt') as f:
        lines = f.read().splitlines()        # Passphrase
    

        # format(1337, 'x') - to hexastring
    
    # COPIED FROM TEST-CLIENT.PY
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    soc.connect(("eitn41.eit.lth.se", 1337))

    # the p shall be the one given in the manual
    p = lines[0].replace(' ', '')
    p = int(p,16)
    print(p)
    g = 2
   
    def agreement():
    # Ta kod från test-client för sockets osv. 
        g_x1 = soc.recv(4096).decode('utf8').strip()
        print ('g**x1:', g_x1)
    # interpret as a number
        g_x1 = int(g_x1, 16)
    # generate g**x2, x2 shall be a random number
        x2 = random.randint(0,10)
    # calculate g**x2 mod p
        g_x2 = pow(g, x2, p)
    # convert to hex-string
        g_x2_str = format(g_x2, 'x')
    # send it
        soc.send(g_x2_str.encode('utf8'))
    # read the ack/nak. This should yield a nak due to x2 being 0
        print ('\nsent g_x2:', soc.recv(4096).decode('utf8').strip())
    #Agree on shared key
        sharedKey = pow(g_x1, x2, p)
        print(sharedKey)
        return sharedKey, x2

    sharedKey,BobExp = agreement()
    gen2,BobExp2 = agreement()
    gen3,BobExp3 = agreement()
    P,Q = calculatePQ(g, gen2, gen3, sharedKey, p)

    Pa  = soc.recv(4096).decode('utf8').strip()
    soc.send(P.encode('utf8'))
    print ('\nsent P:', soc.recv(4096).decode('utf8').strip())

    Qa  = soc.recv(4096).decode('utf8').strip()
    soc.send(Q.encode('utf8'))
    print ('\nsent Q:', soc.recv(4096).decode('utf8').strip())

    #Create Rb - här får vi too big int
    Rb = pow(int(Qa,16) * pow(int(Q,16), -1), BobExp3, p)
    Rb = format(Rb, 'x')
    Ra  = soc.recv(4096).decode('utf8').strip()
    soc.send(Rb.encode('utf8'))
    print ('\nsent Rb:', soc.recv(4096).decode('utf8').strip())
    print ('\nsent authentication:', soc.recv(4096).decode('utf8').strip())

    #Send message - kanske rätt kanske inte
    message = "Hej"
    encryptedMessage = hex(int(message,16) ^ int(str(sharedKey), 16))
    soc.send(encryptedMessage.encode('utf8'))
    receivedMessage = soc.recv(4096).decode('utf8').strip()
    receivedMessage = hex(int(receivedMessage,16) ^ int(str(sharedKey), 16)).decode('utf8')
    print ('\nsent message:', receivedMessage)



def calculatePQ(gen1, gen2, gen3, sharedKey, p):
    b = random.randint(0,10)
    y = sha_hash(sharedKey.to_bytes((sharedKey.bit_length() + 7) // 8, 'big')+ sharedSecret.encode('utf8'))
    print("y :" + y) 

    P= pow(gen3, b, p)
    Q= pow(gen1, b, p) * pow(gen2, int(y,16), p)
   # print("P: " +str(P))
   # print("Q: " + str(Q))
    return format(P, 'x'),format(Q, 'x')


# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    return h

def genX2():
    # TODO
    return 10

if __name__ == '__main__':
    main()
