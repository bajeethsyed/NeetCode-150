#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/submissions/956336558/
# Language: python3
# Date: 2026-04-17


class Solution:
    def maxArea(self, height: List[int]) -> int:
        s=0;e=len(height)-1;maxa=0
        while s<e:
            area = min(height[s],height[e])*abs(s-e)
            if height[s]<height[e]:
                s+=1
            else:
                e-=1
            maxa=max(maxa,area)
        print(maxa)
        return maxa
        
