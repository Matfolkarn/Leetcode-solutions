class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s =''.join(ch for ch in s if ch.isalnum())
        print(s)
        print(len(s))
        print(len(s)//2)
        for i in range(len(s)//2):
            print(s[i], s[len(s)-1-i])
            if s[i].lower() != s[len(s)-1-i].lower():
                return False
        
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))