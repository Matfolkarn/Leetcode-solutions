class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        start = 0
        while start < len(s2):
            if s2[start] in s1:
                s1_temp = s1
                end = start
                while s2[end] in s1_temp:
                    s1_temp = s1_temp.replace(s2[end],"",1)
                    end += 1
                    if len(s1_temp) < 1:
                        return True
                    if end >= len(s2):
                        return False
            start += 1
        return False
