import modulefinder
import mymodule
import platform
import mymodule as kx
import sysconfig
import errno


def greeting(name):
    print ("hello , "+ name)
    
    
mymodule.greeting("karlosh")

person1 = {
    "name": "karlosh",
    "country":"i am from Nepal",
    
}

k = mymodule.person1["country"]
print (k)


k= dir(platform)
print(k)

def greeting(name):
    print("Hello, " + name)

person1 = {
  "name": "rahul",
  "age": 36,
  "country": "india"
}