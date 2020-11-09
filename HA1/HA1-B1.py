# Implement the Luhn algorithm in your favorite language. 
# You will be given a list of card numbers with one digit censored with an “X”. 
# Use your implementation to find the censored digit in order for the card number to be valid. 
# You will be given a list of card numbers, one per line. 
# The answer is the concatenation of all censored digits, in order according to the list.


# Läser en fil med alla kortnummer


def main():
    # Läser in ett kortnummer
    with open('HA1/testin.txt') as f:
        numbers = ''
        lines = f.read().splitlines()
        for line in lines:
            cardNo = line
            # Gör om till array
            cardArray = list(cardNo)
            doubleArray = double(cardArray)

            numbers = numbers + str(summarize(doubleArray))
        print(numbers)



def summarize(doubleArray):

    # Gå över varje element och kollar om värdet är över 10:
    val = 0
    xVal = 1
    for i in range(len(doubleArray)):
        if isinstance(doubleArray[i], str):
            if doubleArray[i].__eq__('2X'):
                xVal = 2
        elif doubleArray[i] >= 10:
            val = val + (doubleArray[i] - 9)
        else:
            val = val + doubleArray[i]
    
    rest = int((val*9) % 10)
    res = rest / xVal

    return int(res)


def double(cardArray):
    print(cardArray)
    # Dubblerar varannan
    for i in range(len(cardArray)-2, -1, -2):
        if (cardArray[i].__eq__('X')):
            cardArray[i] = '2X'
        else:
            cardArray[i] = int(cardArray[i]) + int(cardArray[i])

    #Formattera om arrayen till ints
    for i in range(len(cardArray)-1, 0, -2):
        if (cardArray[i].__eq__('X')):
            cardArray[i] = 'X'
        else:
            cardArray[i] = int(cardArray[i])

    return cardArray



if __name__ == '__main__':
    main()

