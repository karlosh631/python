from os import system
import sys
import pprint
import mymodule
#import system # type: ignore
print ("hi, how are you.")

mytuple = ("egg")
myit = iter(mytuple)

print(next(myit))
print(next(myit))

mytuple = ("apple")
for k in mytuple:
     print(k)
     
     
     
def f():
    global a
    print(a)
    a =2
    
    m= 400
    def myfunc():
        print(m)
        
        myfunc()
        print(m)
        
    exit()
