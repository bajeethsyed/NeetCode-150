#
# Problem: 242. Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/submissions/1977577141/
# Language: python3
# Date: 2026-04-13


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        d={};f={}
        for i in range(len(s)):
            d[s[i]], f[t[i]] = d.get(s[i],0)+1, f.get(t[i],0)+1

        for i in s:
            if d[i]!=f.get(i,0):
                return False
        return True
