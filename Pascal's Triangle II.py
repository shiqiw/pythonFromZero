class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        # ans = [1]
        # if rowIndex == 0:
        #     return ans
        # ans.append(1)
        # if rowIndex == 1:
        #     return ans
        # for i in range (2, rowIndex+1):
        #     tmp = [1]
        #     for j in range (0, i-1):
        #         tmp.append(ans[j] + ans[j+1])
        #     tmp.append(1)
        #     ans = tmp
        # return ans
        
        curr = [1]
        row = 0
        while (row < rowIndex):
            temp = [0] + curr + [0]
            # get familiar with such expression
            # and such as 
            # x[i], x[j] = x[j], x[i]
            curr = [temp[i] + temp[i+1] for i in range(row + 2)]
            row += 1
        return curr
        
        # Python uses a reference counting based GC 
        # Java uses a Generational GC
        