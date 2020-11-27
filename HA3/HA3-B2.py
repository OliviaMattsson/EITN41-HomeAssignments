#authors: Amanda Flote & Olivia Mattsson
from scipy import interpolate 
import numpy as np

def main():
    with open('HA3/testFile.txt') as f:
        lines = f.read().splitlines()
        # Retrieve our private polynomial, 
        # the shares from the other participants + their number and their points on the master polynomial.
        polynomial, shares, master, collab = getinfo(lines)

        # Calculate f(1) - add all terms in the private polynomial
        f1 = sum(polynomial)
        print(f1)

        # Add all the shares given with f1(1) - receives f(1)
        f1 += sum(shares)
        print(f1)

        #Create y-array
        #Calculate the Lagrange polynomial
        x = np.array(collab)
        master.insert(0,f1)
        y = np.array(master)
        poly = interpolate.lagrange(x,y)
        print(poly(0))

def getinfo(lines):
    polynomial = lines[0].split(",")
    polynomial = map(int, polynomial)
    shares = lines[1].split(",")
    shares = map(int, shares)
    master = lines[2].split(",")
    master = map(int, master)
    collab = lines[3].split(",")
    collab = map(int, collab)
    return polynomial, shares, master, collab

if __name__ == '__main__':
    main()
