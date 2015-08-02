# leetcode valid anagram

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
    	# faster
        res = 0
        for c in s:
            res ^= ord(c) # otherwise unsupported operand type(s) for ^=: 'int' and 'unicode'
        for c in t:
            res ^= ord(c)
        return (res == 0)

        # if len(s) != len(t):
        #     return False;
        # # s = s.split() # by default the delimiter is space
        # list(s)
        # list(t)
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # return False