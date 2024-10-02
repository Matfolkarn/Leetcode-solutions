class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for si in s:
            if si in t:
                t = t.replace(si,"",1)
            else:
                return False
        if len(t) > 0:
            return False
        return True