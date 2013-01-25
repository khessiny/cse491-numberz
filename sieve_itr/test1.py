#Yevgeny Khessin
#A39652176
#HW1
#test1
import sieve
#run once to check if value produced is 3. 
def test1():
    s = sieve.sieve() #make a sieve object from file sieve
    i = iter(s) #make iterator
    val=i.next() #run iterator once, put value in val 
    assert val == 3 #check if value is 3. if not 3, fail.
    print "Value should be 3, actual value is:"
    print val


#call test
test1()