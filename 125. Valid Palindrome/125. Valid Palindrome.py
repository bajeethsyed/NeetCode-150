#
# Problem: 125. Valid Palindrome
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-palindrome/
# Language: python3
# Date: 2026-04-15


class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=0;en=len(s)-1
        while st<en:
            if not s[st].isalnum():
                st+=1
            elif not s[en].isalnum():
                en-=1
            else:
                if s[st].lower()==s[en].lower():
                    st+=1
                    en-=1
                else:
                    return False
        return True
