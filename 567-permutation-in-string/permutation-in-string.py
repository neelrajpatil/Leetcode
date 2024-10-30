class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a counter for s1
        count_s1 = Counter(s1)
        # slide the window through s2, where the window is the len of s1
        for i in range(len(s2)-len(s1)+1):
            count_window = Counter(s2[i:i+len(s1)])

            # check if counter for current window is the same as s1
            if count_window == count_s1:
                return True
        
        return False
        