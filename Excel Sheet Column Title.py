# string.split()

# Leetcode  Excel Sheet Column Title
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        # iterative solution, fastest
        ans = ''
        c = 'A'
        while n > 0:
            res = n % 26
            n = n / 26
            if res != 0:
                # the scope of c makes using chr(c) here gives error
                c = chr(65 + res - 1)
            else:
                c = 'Z'
                # there is no -- in python
                n -= 1
            ans = c + ans
        return ans

        # iterative solution 2
        # ans = ''
        # while n > 0:
        #     c = chr( (n-1) % 26 + 65)
        #     ans = c + ans
        #     n = (n-1) / 26
        # return ans
        
        # recursive solution
        # ans = ''
        # if n > 26:
        #     ans = self.convertToTitle((n-1)/26)
        # ans += chr(65 + (n-1)%26)
        # return ans
