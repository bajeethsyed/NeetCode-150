#
# Problem: 83. Remove Duplicates from Sorted List
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/1985615936/
# Language: python3
# Date: 2026-04-22


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer=head
        while pointer and pointer.next:
            if pointer.val==pointer.next.val:
                pointer.next=pointer.next.next
            else:
                pointer=pointer.next
        return head
            
        
