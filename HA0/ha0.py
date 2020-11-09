# Some assignments will require you to interpret and print data in different ways, 
# more specifically as integers, (hexadecimal) strings and byte arrays. 
# This can lead to some confusion and headache, though the conversion typically only requires one line of code. 
# In this assignment you shall implement 6 functions to convert between these different representations. 
# You will also use the SHA-1 hash function. 
import array
import hashlib
import binascii

def main():

    value = str(input("Enter the value:"))
    print("Converting " + value + ":")
    
    # print(hexa_to_int(sha_hash(hexa_to_byte(int_to_hexa(int(value))))))
    print(hexa_to_int(sha_hash(hexa_to_byte(str(value)))))
    # print(hexa_to_int(sha_hash(bytearray(value.encode()))))
    # print(hexa_to_int(byte_to_hexa(value)))
    # print(sha_hash(hexa_to_byte(int_to_hexa(int(value)))))
    # print(hexa_to_int(int_to_hexa(int(value))))

# Int to hexadecimal string
def int_to_hexa(inputVal):
    print("Int to hexadecimal: " + hex(inputVal).lstrip('0x'))
    return hex(inputVal).lstrip('0x')

# Hexadecimal string to int
def hexa_to_int(inputVal):
    print("Hexadecimal (hash) to int: ")
    return int(inputVal, 16)

# Hexadecimal string to byte array
def hexa_to_byte(inputVal):
    # val = array.array('B', inputVal.encode())
    
    while len(inputVal) < 8:
        inputVal = '0' + inputVal
    print("modified hexadec: " + inputVal)
    val = binascii.unhexlify(inputVal)
    print("Hexa to byte array: " + str(val))
    return val

# Byte array to hex
def byte_to_hexa(inputVal):
    print(inputVal)
    val = bytes.fromhex(inputVal)
    print("Byte to hexa: " + str(binascii.hexlify(val)))
    return binascii.hexlify(val)

# Byte array to hash
def sha_hash(inputVal):
    h = hashlib.sha1(inputVal).hexdigest()
    print("Sha hash: " + h)
    return h
    



if __name__ == '__main__':
    main()