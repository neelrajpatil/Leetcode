class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Returns:
            - true if str can be segmented into words from wordDict
            - False if not
        
        Test case:
            INVALID TEST CASE - s="applepen" wordDict=["app","apple","pen"]

        Constraints:
            - same word can be repeated
        """

        # Approach 1: 
        # use a hash map to check validity
        # make a list of valid words in s with their start and end index Time O(n^2)
        # find if a combination of these valid words segments s completely

        # Approach 2: 
        
        # make a cache 
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        # begin from the end of s
        for i in range(len(s)-1, -1,-1):
            # check each word in wordDict if it matches
            for w in wordDict:
                if (len(s)-i) >= len(w) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i] == True:
                    break
        return dp[0]
                         