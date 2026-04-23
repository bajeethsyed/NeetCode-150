#
# Problem: 977. Squares of a Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/solutions/
# Language: python3
# Date: 2026-04-23


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=0;e=len(nums)-1
        l=[]
        while s<=e:
            if abs(nums[s])<=abs(nums[e]):
                l.append(nums[e]**2)
                e-=1
            else:
                l.append(nums[s]**2)
                s+=1
        print(l)        
        return l[::-1]


