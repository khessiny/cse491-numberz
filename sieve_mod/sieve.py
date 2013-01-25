#Yevgeny Khessin
#A39652176
#HW1
# an implementation of Eratosthenes' Sieve using a a Python module

listprimes = [2]

def primecheck(primes, n): #function defition of checking if number is prime
    for i in primes:   #for all numbers in primes list 
        if n % i == 0:  #if modulus is 0 
            return False   #return false
    return True  #if not, return true

def next(): #next definition 
    counter = listprimes[-1] + 1 #
    while 1:
        if primecheck(listprimes, counter):
            listprimes.append(counter)
            return counter

        counter += 1
