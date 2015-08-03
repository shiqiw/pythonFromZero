# Python self
# There is no less verbose way. 
# Always use self.x to access the instance attribute x. 
# Note that unlike this in C++, self is not a keyword, though. 
# You could give the first parameter of your method any name you want, 
# but you are strongly advised to stick to the convention of calling it self.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lengA = self.length(headA)
        lengB = self.length(headB)
        if lengA > lengB:
            return self.intersectHelper(headA, headB, lengA, lengB)
        else:
            return self.intersectHelper(headB, headA, lengB, lengA)
        
    def length(self, head):
        l = 0
        iter = head
        while iter != None:
            l += 1
            iter = iter.next
        return l
        
    def intersectHelper(self, headA, headB, lengA, lengB):
        diff = lengA - lengB
        while diff != 0:
            headA = headA.next
            diff -= 1
        while lengB != 0:
            if headA == headB:
                return headA
            lengB -= 1
            headA = headA.next
            headB = headB.next
        return None
            