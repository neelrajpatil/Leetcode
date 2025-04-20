"""
"abcabcbb" -> 3
"bbbbb" -> 1

"aabcc" -> 3

Constraints
0 <= s.length <= 5 * 10^4
s {a:z,A:Z,spaces,symbols, digits,}

Approaches
Brute Force Time O(n^2) Space(n)
    every possible start point
        every possible end point
            check if all chars are unique
Sliding Window Time O(n) Space(n)
    expand right until invalid substring
        if invalid
            shorten left until valid

"tmmzuxt"
len(s) = 7
l 0
r 2
all_chars (t,m)
res 3

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if len(s) < 2:
            return len(s)
        l = 0
        r = 1
        all_chars = set()
        all_chars.add(s[0])
        res = 1
        while(r<len(s)):
            r += 1 #expand window
            if s[r-1] in all_chars: # if invalid
                while s[l] != s[r-1]:  # keep incrementing until duplicate char is found
                    all_chars.remove(s[l])
                    l += 1
                l += 1
            else: # if valid
                all_chars.add(s[r-1])
                res = max(res,r-l)
        return res