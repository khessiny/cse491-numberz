#Yevgeny Khessin
#A39652176
#HW1
#test1
import sieve
#run 3 times to check if value is  7
def test2():
    s = sieve.sieve() #make a sieve object from file sieve
    i = iter(s) #make iterator
    val=i.next() #run iterator once, put value in val 
    val=i.next() #run iterator once, put value in val 
    val=i.next() #run iterator once, put value in val     
    
    assert val == 7 #check if value is 7. if not 7, fail. 
    print "Value should be 7, actual value is:"
    print val

#call test
test2()