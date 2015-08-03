# Python basics
# Comments in Python

# Variable
age = 6
intro = 'I am '

# Built-in len()
length = len(intro)

# Built-in str()
# Concatenation of string
print(intro + str(age))

# Built-in print()
print(length)

# Formatting string
hour = 10
minute = 45
print("current time is %s : %s" % (hour, minute))

# string.format() built-in
# {[field name] ["!" conversion] [":" format spec]}
print("or write in this way {0:4d}:{1:4d}".format(hour, minute))

print("""It's saied triple quote can diplay
what ever I want.""")

# Exponential
print("Just to show ** is exponential: 5**2 = %d" %(5**2))





# Python use dent to indicate scope
# strict on style
# True False and None
prize = None

if hour < 11 :
    prize = True

# int() built-in
if prize:
    gift = int( input("How much money would you like?\n"))
    print("gift card %.2f" % gift)

# Classes import (file import)
import datetime

# For more specific display, there is strftime(), %b, %B, %y, %a and %A
# Similarly strftime accepts %H %I %p %m and %S
print (datetime.date.today())
print (datetime.datetime.now())

# In python, else if is called elif
judge = int(input("How old r u?\n"))
if judge < 12:
    print("you are a child.\n")
elif judge < 18:
    print("you are a teenager.\n")
else:
    print("you are an adult.\n")

# The logic 'and' in python is called -- and
# Similar with 'or'





# turtle is the class that can draw
import turtle
turtle.color('green')
turtle.forward(100)

# Right and left is to rotate in degree
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)

for steps in range(1,4):
    print(steps)

# range(start, end, interval)
for steps in range(1, 10, 2):
    print(steps)

# for steps in [1, 2, 3]: ...

# Similarly while loop
