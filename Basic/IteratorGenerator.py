# Iterator -> __iter__() and next()
# Iterable -> can use __iter__() to obtain iterator
class MyRange:
	def __init__(self, n):
		self.index = 0
		self.n = n

		def __iter__(self):
			return self

		def next(self):
			if self.index < self.nval = self.index:
				self.index += 1
				return val
			else:
				raise StopIteration()

# If both iterable and is iterator, can only iterate once
mr = MyRange(3)
for i in mr:
	print(i)

class Zrange:
	def __init__(self, n):
		self.n = n

	def __iter__(self):
		return ZrangeIterator(self.n)

class ZrangeIterator:
	def __init__(self, n):
		self.i = 0
		self.n = n

	def __iter__(self):
		return self

	def next(self):
		if self.i < self.n:
			i = self.i
			self.i += 1
			return i
		else:
			raise StopIteration()

zrange = Zrange(3)
print([i for i in zrange])
print([i for i in zrange])





# Genrator use yield give back result
def Xrange(n):
	i = 0
	while i < n:
		yield i
		i += 1

# Does not yield
xrange = Xrange(3)
# Yield i = 0
print(xrange.next())
# yield i = 1
print(xrange.next())

# This generator is both iterable and is iterator
gen = (i for i in range(50) if i%2)

# Simple generator, using permuation as example

def permutation(li):
	if len(li) == 0:
		yield li
	else:
		for i in range(len(li)):
			li[0], li[i] = li[i], li[0]
			for item in permutation(li[1:]):
				yield [li[0]] + item

for item in permutation(range(3)):
	print(item)

# Send() and close() in generator
# Send is used to send values into a generator that just yielded
def doubleInputs():
	while True:
		x = yield
		yield x*2

di = doubleInputs()
di.next()
di.send(10)
di.next()

# After calling close() can not send
di.send(6)
