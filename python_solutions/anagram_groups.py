class Solution:
    def is_anagram(self,l1: str, l2: str):
        if len(l1) != len(l2):
            return False
        l1_s = "".join(sorted(l1))
        l2_s = "".join(sorted(l2))
        for i in range(len(l1_s)):
            if l1_s[i] != l2_s[i]:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for l in strs:
            already_exists = False
            for i in range(len(result)):
                r = result[i]
                print(self.is_anagram(l,r[0]))
                if self.is_anagram(l,r[0]):
                    result[i].append(l)
                    already_exists = True
                    break
            if not already_exists:
                result.append([l])
        return result