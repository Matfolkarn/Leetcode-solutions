class Solution:
    def countSubstrings(self, s: str) -> int:
        pal = 0
        for i in range(len(s)):
            # Odd length
            pal += 1
            lp = i -1
            rp = i + 1
            substr = s[i]
            while lp >= 0 and rp < (len(s)) and s[lp] == s[rp]:
                substr = s[lp] + substr + s[rp]
                lp -= 1
                rp += 1
                pal +=1

            # Even length
            if i + 1 >= (len(s)):
                continue
            if s[i] != s[i+1]:
                continue
            pal += 1
            lp = i -1
            rp = i + 2
            substr = s[i] + s[i + 1]
            while lp >= 0 and rp < (len(s)) and s[lp] == s[rp]:
                substr = s[lp] + substr + s[rp]
                lp -= 1
                rp += 1
                pal +=1
        return pal
