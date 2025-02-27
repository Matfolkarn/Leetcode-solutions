class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set()
        for i in range(1,27):
            valid.add(str(i))

        dp = {len(s) : 1}

        for i in range(len(s) -1 , -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] + s[i+1]) in valid:
                dp[i] += dp[i +2]
        return dp[0]
            

