class Solution:
    def reverseWords(self, s: str) -> str:
        # remove leading or trailing spaces
        start, end = 0, len(s)-1
        while True:
            if s[start] == ' ':
                start += 1
            elif s[end] == ' ':
                end -= 1
            else:
                break
        s = s[start:end+1]

        # remove multiple spaces
        words = s.split(" ")
        result = []
        for i in words:
            if not i == "": 
                result.append(i)
        result.reverse()
        return " ".join(result)