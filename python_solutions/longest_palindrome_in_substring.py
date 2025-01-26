class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        pal = ""


        for i in range(len(s)):
            # Odd length
            lp = i -1
            rp = i + 1
            substr = s[i]
            while lp >= 0 and rp < (len(s)) and s[lp] == s[rp]:
                substr = s[lp] + substr + s[rp]
                lp -= 1
                rp += 1
            if len(pal) < len(substr):
                pal = substr

            # Even length
            if i + 1 >= (len(s)):
                continue
            if s[i] != s[i+1]:
                continue
            lp = i -1
            rp = i + 2
            substr = s[i] + s[i + 1]
            while lp >= 0 and rp < (len(s)) and s[lp] == s[rp]:
                substr = s[lp] + substr + s[rp]
                lp -= 1
                rp += 1
            if len(pal) < len(substr):
                pal = substr

        return pal
