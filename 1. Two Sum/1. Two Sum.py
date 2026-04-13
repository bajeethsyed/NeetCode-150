#
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/submissions/1977584618/
# Language: python3
# Date: 2026-04-13


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if d.get(nums[i],0):
                return [d.get(nums[i],0)-1,i]
            d[target-nums[i]]=i+1

        
