#Yevgeny Khessin
#A39652176
#HW1
# an implementation of Eratosthenes' Sieve using a Python generator

def primecheck(primes, n): #function defition of checking if number is prime
    for i in primes:   #for all numbers in primes list 
        if n % i == 0:  #if modulus is 0 
            return False   #return false
    return True  #if not, return true

def sieve():   #sieve function 
    listprimes = [2]  #list of primes starting at 2 
    counter = listprimes[-1] + 1   #go one back and add 1 
    while 1: #endless while loop 
        if primecheck(listprimes, counter):  #check if number is prime 
            listprimes.append(counter)  #add it to list
            yield counter  #return the value 

        counter += 1   #increment counter