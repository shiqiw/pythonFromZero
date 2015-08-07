class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if len(s) < 2:
            return True
        s = s.lower()
        sc = list(s)
        i = 0
        j = len(sc) - 1
        while i < j:
            # if do not use self here, cause global name undefined error
            if not self.isAlNum(sc[i]):
                i += 1
                continue
            if not self.isAlNum(sc[j]):
                j -= 1
                continue
            if sc[i] != sc[j]:
                return False
            i += 1
            j -= 1
        return True
       
    # the representation of characters in Python is Unicode, not ASCII
    def isAlNum(self, c):
        return c.isalpha() or c.isdigit()