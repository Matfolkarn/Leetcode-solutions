class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l = 0
        nbr_most_freq_char = 0
        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)
            nbr_most_freq_char = max(nbr_most_freq_char, count[s[r]])

            if r - l + 1 - nbr_most_freq_char > k:
                count[s[l]] -= 1
                l += 1
        
        return r - l + 1

            
