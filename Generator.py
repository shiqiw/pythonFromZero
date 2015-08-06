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

# send() and close() in generator, TBC
