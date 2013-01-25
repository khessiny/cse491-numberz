#Yevgeny Khessin
#A39652176
#HW1
# an implementation of Eratosthenes' Sieve using a Python iterator

def primecheck(primes, n): #function defition of checking if number is prime
    for i in primes:   #for all numbers in primes list 
        if n % i == 0:  #if modulus is 0 
            return False   #return false
    return True  #if not, return true

class sieve(object):
    def __init__(self):  #initializtion
     self.listprimes = [2] #list of primes starting at 2 

    def __iter__(self): #iterator
     return self   #returns itself

    def next(self): #iterator next
     counter = self.listprimes[-1] + 1  #go back 1 and add 1 
     while 1: #endless while loop 
         if primecheck(self.listprimes, counter): #if it is a prime number
             self.listprimes.append(counter) #add it to the list 
             return counter #return the value 
         counter += 1 #increment counter






