# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        # is None, is leaf, has one child, has two child
        # if root == None:
        #     return 0;
        # if root.left == None and root.right == None:
        #     return 1;
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)
        # if left == 0:
        #     return right + 1;
        # if right == 0:
        #     return left + 1
        # return min(left, right) + 1;
        
        # if not root: 
        #     return 0
        # # the usage of phython map
        # d = map(self.minDepth, (root.left, root.right))
        # # what does this or do?
        # return 1 + (min(d) or max(d))
        
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)

        # Functional approach of programming
        # map(aFunction, aSequence)
        # filter(aFunction, aSequence)
        # reduce(aFunction, aSequence)
        # lambda
        # list comprehension
        # http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php