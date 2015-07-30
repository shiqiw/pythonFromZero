import sys

def getName():
    # input in python 2.x interprets input as python code, use input() will cause name not defined error
    # need to use raw_input()
    # ZeroDivisionError is a case that can be used with except
    try:
        secret = str(input('what is your name?'))
        return secret
    except:
	error = sys.exc_info()[0]
	print(error)
        print('==== Wrong input type, should be quoted with \'\' if using input()====')
	return 'Bad name'
	# sys.exit()
    # if not exit or return, code will continue execute
    print('This msg will always not be displayed')

def printName(secret):
    if secret == 'Bad name':
	print('Bad input')
    else:
        print('Hello ' + secret + '!')
    return
