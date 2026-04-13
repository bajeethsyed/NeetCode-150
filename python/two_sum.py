# ======================================
# LeetCode Problem: two sum
# Language: python3
# Link: https://leetcode.com/problems/two-sum/
# Synced by: LinkCode
# Date: 4/13/2026, 11:15:11 PM
# ======================================


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if d.get(nums[i],0):
                return [d.get(nums[i],0)-1,i]
            d[target-nums[i]]=i+1

        