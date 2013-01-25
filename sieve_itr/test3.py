#Yevgeny Khessin
#A39652176
#HW1
#test3
import sieve
#run once to make sure iterator is not at 2
def test3():
    s = sieve.sieve() #make a sieve object from file sieve
    i = iter(s) #make iterator
    val = i.next() #run iterator once, put value in val

    assert val != 2 #check if value not 2 
    print "Value should not be 2, actual value is:"
    print val


#call test3
test3()