class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        l, r = 0, 0
        shortest = ""

        while True:
            res_sub = s[l:r]
            substr = list(s[l:r])
            cont_all = True
            for ts in t:
                if ts in substr:
                    substr.remove(ts)
                else:
                    cont_all = False
            
            if cont_all:
                l += 1
                if len(shortest) > len(res_sub) or len(shortest) == 0:
                    shortest = res_sub
            else:
                if r == len(s):
                    return shortest
                r += 1
