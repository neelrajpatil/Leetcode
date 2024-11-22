class Solution:

    def __init__(self, w: List[int]):
        self.prob = []
        self.total_sum = 0

        for i in w:
            self.total_sum += i
            self.prob.append(self.total_sum)

    def pickIndex(self) -> int:
        target = random.randint(1,self.total_sum)

        l = 0
        r = len(self.prob) - 1
        while l < r:
            mid = (l + r)//2
            if self.prob[mid] < target:
                l = mid + 1
            else:
                r = mid
            
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()