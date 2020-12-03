# OTR
# By Amanda Flote & Olivia Mattsson

import hashlib
import socket





def main():
    # Read a file with the content: 
    with open('HA4/testfiles/p.txt') as f:
        lines = f.read().splitlines()        # Passphrase
    sharedSecret = "eitn41 <3"

        # format(1337, 'x') - to hexastring
    
    # COPIED FROM TEST-CLIENT.PY
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    soc.connect(("eitn41.eit.lth.se", 1337))

    # the p shall be the one given in the manual
    p = lines[0].replace(' ', '')
    p = int(p,16)
    print(p)
    g = 2
    # Ta kod från test-client för sockets osv. 
    g_x1 = soc.recv(4096).decode('utf8').strip()
    print ('g**x1:', g_x1)
    # interpret as a number
    g_x1 = int(g_x1, 16)

    # generate g**x2, x2 shall be a random number
    x2 = genX2()
    # calculate g**x2 mod p
    g_x2 = pow(g, x2, p)
    # convert to hex-string
    g_x2_str = format(g_x2, 'x')
    # send it
    soc.send(g_x2_str.encode('utf8'))
    # read the ack/nak. This should yield a nak due to x2 being 0
    print ('\nsent g_x2:', soc.recv(4096).decode('utf8').strip())

# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    return h

def genX2():
    # TODO
    return 10

if __name__ == '__main__':
    main()
