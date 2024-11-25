class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        return the no of unmatched parenthesis

        s="((()))))" =>  3
        s="))())())" =>

        Constraints:
            - 
        """

        # Approach 1: Stack, iterate through s, return len(stack) Time O(n) Space (n)

        stack = []

        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)