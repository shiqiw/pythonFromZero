# Leetcode min stack

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.reg = []
        self.mins = []
        self.size = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.reg.append(x)
        if self.size == 0 or self.mins[-1] >= x:
            self.mins.append(x)
        self.size += 1

    # @return nothing
    def pop(self):
        x = self.reg[-1]
        del(self.reg[-1])
        if self.mins[-1] == x:
            del(self.mins[-1])
        self.size -= 1

    # @return an integer
    def top(self):
        return self.reg[-1]

    # @return an integer
    def getMin(self):
        return self.mins[-1]