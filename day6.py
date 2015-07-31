# string.split()

# Leetcode practice Excel Sheet Column Title
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        # iterative solution, faster than recursive one
        ans = ''
        c = 'A'
        while n > 0:
            res = n % 26
            n = n / 26
            if res != 0:
                # why use chr(c) here gives error
                c = chr(65 + res - 1)
            else:
                c = 'Z'
                # there is no -- in python
                n -= 1
            ans = c + ans
        return ans
        
        # recursive solution
        # ans = ''
        # if n > 26:
        #     ans = self.convertToTitle((n-1)/26)
        # ans += chr(65 + (n-1)%26)
        # return ans
