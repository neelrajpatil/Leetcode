class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        
        """
        count = 0
        res = []
        for char in s:
            if char == "(":
                count += 1
                res.append(char)
            elif char == ")" and count >0:
                count -= 1
                res.append(char)
            elif char != ")":
                res.append(char)

        filtered_res = []
        for char in res[::-1]:
            if char == "(" and count >0:
                count -= 1
            else:
                filtered_res.append(char)
        
        return "".join(filtered_res[::-1])