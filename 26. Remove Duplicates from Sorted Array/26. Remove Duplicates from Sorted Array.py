#
# Problem: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1985631447/
# Language: python3
# Date: 2026-04-22


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=0;e=1
        while e<len(nums):
            if nums[s]==nums[e]:
                e+=1
            else:
                s+=1
                nums[s],nums[e]=nums[e],nums[s]
                e+=1
        return len(nums[:s+1])
