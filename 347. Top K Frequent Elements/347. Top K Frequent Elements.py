#
# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Language: python3
# Date: 2026-04-13


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={};l=[[] for i in range(len(nums)+1)];r=[]
        
        for i in nums:
            s[i]=s.get(i,0)+1
        
        for i,j in s.items():         # use bucket sorting type  
            l[j].append(i)  
        
        for i in l[::-1]:
            for j in i:
                r.append(j)
                k-=1
                if k==0:
                    return r


# ----- optimization ------
        s={};l=[[] for i in range(len(nums)+1)];r=[]
        
        for i in nums:
            s[i]=s.get(i,0)+1
        
        for i,j in s.items():         # use bucket sorting type  
            l[j].append(i) 

        for i in l[::-1]:
            n=len(i)
            if n: 
                if n>k:
                    r.extend(i[:k+1])
                    k=0
                elif n<=k:
                    r.extend(i)
                    k-=n
                if k==0:
                    return r
        return r
