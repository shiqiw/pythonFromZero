# Pytho  function
def printHello(msg):
    print('hello ' + msg)
    return

printHello('world')
# similarly, params are separated by comma

# import other files
import helper5

def main():
    secret = helper5.getName()
    helper5.printName(secret)
    return

main()
