# Luhn algorithm in Python
# Amanda Flote & Olivia Mattsson


def main():
    # Reads the file
    with open('HA1/quizLuhn.txt') as f:
        numbers = ''
        lines = f.read().splitlines()
        for line in lines:
            cardNo = line
            # Converts to an array
            cardArray = list(cardNo)
            # Retrieves the int values 
            intArray = double(cardArray)
            # Adds the result to the answer string
            numbers = numbers + str(summarize(intArray))

        print(numbers)



def summarize(intArray):
    val = 0
    xVal = 1
    # Iterate over every value to add it to val:
    for i in range(len(intArray)):
        if isinstance(intArray[i], str):
            if intArray[i].__eq__('2X'):
                xVal = 2
        elif intArray[i] >= 10:
            val = val + (intArray[i] - 9)
        else:
            val = val + intArray[i]
    
    # Computes the value for X
    res = int((val*9) % 10)
    
    # If we have 2X:
    if xVal == 2:
        # If there's an uneven number, we need to add 9 again to get the two numbers combined
        if res%2 != 0:
            res = (res + 9)
        res = int(res/2)

    return int(res)


def double(cardArray):
    
    # Doubles every other value, counting from the rightmost.
    for i in range(len(cardArray)-2, -1, -2):
        if (cardArray[i].__eq__('X')):
            cardArray[i] = '2X'
        else:
            cardArray[i] = int(cardArray[i]) + int(cardArray[i])

    # Formats the other values, except X, to ints as well
    for i in range(len(cardArray)-1, 0, -2):
        if (cardArray[i].__eq__('X')):
            cardArray[i] = 'X'
        else:
            cardArray[i] = int(cardArray[i])

    return cardArray



if __name__ == '__main__':
    main()

