#Yevgeny Khessin
#A39652176
#HW1
# an implementation of Eratosthenes' Sieve using a Python generator
import sieve
#create zip of 1 through 4, and run sieve on it, printing results
for n, i in zip(range(4), sieve.sieve()):
    print i