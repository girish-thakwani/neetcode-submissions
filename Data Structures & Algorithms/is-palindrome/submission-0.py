class Solution:
    def isPalindrome(self, s: str) -> bool:
        def al(a):
            if (ord('A')<=ord(a)<=ord('Z') or ord('a')<=ord(a)<=ord('z') or ord('0')<=ord(a)<=ord('9')) : return True
            return False

        l=0
        r=len(s)-1
        while l<r:
            while l<r and not al(s[l]):
                l+=1
            while r>l and not al(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
            
