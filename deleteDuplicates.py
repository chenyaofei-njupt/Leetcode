"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prob = head
        while prob and prob.next :   
			if prob.next.val == prob.val:
				prob.next =prob.next.next
            else:
                prob = prob.next            
        return head