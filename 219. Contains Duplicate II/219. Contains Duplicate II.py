#
# Problem: 219. Contains Duplicate II
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate-ii/description/
# Language: python3
# Date: 2026-04-15


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i,j in enumerate(nums):
            if d.get(j,0):
                if abs(i-d[j]+1)<=k: 
                    return True
            d[j]=i+1
        return False
            

