#
# Problem: 238. Product of Array Except Self
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-array-except-self/submissions/1978630837/
# Language: python3
# Date: 2026-04-14


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[1]
        pre,pos=1,1
        for i in range(1,len(nums)):
            pre=pre*nums[i-1]
            r.append(pre)
        for i in range(len(nums)-2,-1,-1):
            pos*=nums[i+1]
            r[i]*=pos
        return r
