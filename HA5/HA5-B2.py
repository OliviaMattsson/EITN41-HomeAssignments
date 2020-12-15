# Identity based encryption scheme
# By Olivia Mattsson and Amanda Flote

# Inputs:
identity = 'walterwhite@crypto.sec'
p = '9240633d434a8b71a013b5b00513323f'
q = 'f870cfcd47e6d5a0598fc1eb7e999d1b'
encryptedBits = ['83c297bfb0028bd3901ac5aaa88e9f449af50f12c2f43a5f61d9765e7beb2469', '519fac1f8ac05fd12f0cbd7aa46793210988a470d27385f6ae10518a0c6f2dd6', '2bda0d9c8c78cb5ec2f8c038671ddffc1a96b5d42004104c551e8390fbf4c42e']

#Decryption:
def decrypt(r, m):
    # Given priate key r and encrypted message m:
    # if r^2 is equivalent to a (mod n), then set y = s_i,1 otherwise y = s_i,2

    # Plaintext bit x_i can be recovered from y + 2r mod n using Jacobi:


    # Decryption fail if gcd(1 + rt^-1) mod n is not 1 
    return

# Calculate the Jacobi symbol, based on the Wikipedia page: https://en.wikipedia.org/wiki/Jacobi_symbol#Properties
def jacobi(n, k):
    if k <= 0 and k % 2 != 1:
        return
    n = n % k
    t = 1
    while n != 0:
        while n % 2 == 0:
            n = n / 2
            r = k % 8
            if r == 3 or r == 5:
                t = -t
    n, k = k, n
    if n % 4 == 3 and k % 4 == 3:
        t = -t
    n = n % k
    if k == 1:
        return t 
    else:
        return 0
    return 

def pkg():
    # using Cock's Encryption Scheme:
    return

