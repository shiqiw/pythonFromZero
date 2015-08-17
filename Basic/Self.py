class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

class Test:
    def prt(this):
        print(this)
        print(this.__class__)
 
t = Test()
t.prt()

# this is wrong, t.prt() equals Test.prt(t)
class Test:
    def prt():
        print(self)
 
t = Test()
t.prt()

class Test:
    def prt():
        print(__class__)
Test.prt()

class Parent:
    def pprt(self):
        print(self)
 
class Child(Parent):
    def cprt(self):
        print(self)
c = Child()
c.cprt()
c.pprt()
p = Parent()
p.pprt()

class Desc:
    def __get__(self, ins, cls):
        print('self in Desc: %s ' % self )
        print(self, ins, cls)
class Test:
    x = Desc()
    def prt(self):
        print('self in Test: %s' % self)
t = Test()
t.prt()
t.x # same as Text.x
# 这里调用的是t.x，也就是说是Test类的实例t的属性x，由于实例t中并没有定义属性x，所以找到了类属性x，而该属性是描述符属性，为Desc类的实例而已，所以此处并没有顶用Test的任何方法。