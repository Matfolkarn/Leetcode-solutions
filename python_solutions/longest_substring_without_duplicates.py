class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        longest = 0
        bottom = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[bottom])
                bottom += 1
            charSet.add(s[i])
            print(charSet)
            longest = max(longest, len(charSet))
        return longest
