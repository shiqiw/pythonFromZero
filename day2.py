# Know the frequent used classes
import datetime

print (datetime.date.today())
# for more specific display, there is strftime(), %b, %B, %y, %a and %A
print (datetime.datetime.now())
# similarly strftime accepts %H %I %p %m and %S

# in python, else if is called elif
judge = int(input("How old r u?\n"))
if judge < 12:
    print("you are a child")
elif judge < 18:
    print("you are a teenager")
else:
    print("you are an adult")

# the logic 'and' in python is called -- and
# similar with 'or'

# turtle is the class that can draw
import turtle
turtle.color('green')
turtle.forward(100)

# right and left is to rotate in degree
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)

for steps in range(1,4):
    print(steps)

# range(start, end, interval)
for steps in range(1, 10, 2):
    print(steps)

# for steps in [1, 2, 3]: ...
# similarly while loop
