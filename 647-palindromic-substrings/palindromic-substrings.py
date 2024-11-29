"""

Question:

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

example 1: s = "abc"
"a"
"b"
"c"

example 2: s = "aaa"
"a"
"a"
"a"
"aa"
"aa"
"aaa"

example 3: "ababac"
"bb"
"abba"
"a"
"a"
"b"
"b"
"c"


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

"""

class Solution:
    def checkPalindrome(self, s:str)-> bool:
        if len(s) == 2 and s[0] == s[1]:
            return True
        if len(s) == 3 and s[0] == s[2]:
            return True

        return False


    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        # "ababac"
        # Approach 3: 

        # ini variables
        counter = 0 # 4
        n=len(s) # 6
        # two pointers 
        l = 0 # 4
        r = 1 # 6
        
        # looping until l ==n-2 and r == n-1
        while l <=n-2 and r <= n-1: # l <= 4 r <= 5
            # considering first 2 characters
            # if it is palindrome
            if self.checkPalindrome(s[l:r+1]):
                counter += 1
                temp_l = l - 1
                temp_r = r + 1
                # keep moving l and r outwards until we hit the boundary or encounter a non-palindrome
                while temp_l >= 0 and temp_r < n:
                    if s[temp_l] != s[temp_r]:
                        break
                    counter += 1
                    temp_l -= 1
                    temp_r += 1
            # increment r, considering 3 characters
            r += 1 #/
            if r < n and self.checkPalindrome(s[l:r+1]):
                # keep moving l and r outwards until we hit the boundary or encounter a non-palindrome
                counter += 1
                temp_l = l - 1 # 1
                temp_r = r + 1 # 5
                # keep moving l and r outwards until we hit the boundary or encounter a non-palindrome
                while temp_l >= 0 and temp_r < n:
                    if s[temp_l] != s[temp_r]:
                        break
                    counter += 1
                    temp_l -= 1
                    temp_r += 1

            # increment left
            l += 1

        return counter + n # 4 + 6 = 10


    # Approach 1: Brute Force Time O(n)

    # Approach 2:
    # find evaluate substring which is palindrome
    # two pointers l r, moving towards opposite ends
    # while l <=r
        # for each substring check if it is a palindrome
            # sub-substring palindrones
            # aabbaa
            # abcdcba