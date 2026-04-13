#
# Problem: 217. Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/description/
# Language: python3
# Date: 2026-04-13


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if d.get(i,0):
                return True
            else:
                d[i]=1
        return False
