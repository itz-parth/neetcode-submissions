class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for ch in s:
            if ch.isalnum():
                s2 += ch.lower()

        st, end = 0, len(s2) - 1

        while end > st:
            if s2[st] != s2[end]:
                return False
            st += 1
            end -= 1
        
        return True