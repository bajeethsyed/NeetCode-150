#
# Problem: 49. Group Anagrams
# Difficulty: Medium
# Link: https://leetcode.com/problems/group-anagrams/
# Language: python3
# Date: 2026-04-13


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Method-1
        r={}
        for i in strs:
            d=[0]*26
            for j in i:
                d[ord(j)%97]+=1
            r[tuple(d)]=r.get(tuple(d),[])+[i]            # Key must always in Immutable Data-Types (Strings, Tuples)
        return list(r.values())

        # Method - 2
        r={}
        for i in strs:
            v="".join(sorted(i))
            if r.get(v,0):
                r[v].append(i)
            else:
                r[v]=[i]
        return list(r.values())

