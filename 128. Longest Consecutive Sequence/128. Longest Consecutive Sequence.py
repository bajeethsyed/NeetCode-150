#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1979380105/
# Language: python3
# Date: 2026-04-15


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in numSet:
            if i-1 not in numSet:
                length=0
                while (i+length) in numSet:
                    length+=1
                longest = max(longest,length)
        return longest
