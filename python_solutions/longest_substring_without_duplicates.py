class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):


            dupl = False
            current_characters = []
            ii = 0
            while not dupl:    
                if ii + i >= len(s):
                    return longest
                
                character = s[i + ii]
                if character not in current_characters:
                    longest = max(longest, ii+1)
                else:
                    dupl = True
                current_characters.append(character)

                ii += 1
