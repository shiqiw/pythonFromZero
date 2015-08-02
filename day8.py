# leetcode compare version number
# learn usage of map()
# learn list operation

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        # beware of tailing zero
        v1, v2 = self.helper(version1), self.helper(version2)
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0
        
    def helper(self, v):
        vn = map(int, v.split('.')) # map accept lambda function in first param
        i = len(vn)-1
        while i>= 0 and vn[i] == 0:
            i -= 1
        return vn[:i+1]
        