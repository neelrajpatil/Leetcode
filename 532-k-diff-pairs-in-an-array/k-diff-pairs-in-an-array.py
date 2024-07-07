class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        count = 0
        
        for num in counter:
            if k > 0:
                if num + k in counter:
                    count += 1
            elif k == 0:
                if counter[num] > 1:
                    count += 1
        
        return count

        # counter = {}

        # for num in nums:
        #     if num in counter:
        #         counter[num] += 1
        #     else:
        #         counter[num] = 1
        

        # valid_count = 0
        # for num in nums:
        #     if (num+k) in counter:
        #         valid_count += counter[(num+k)]
        #     elif (num-k) in counter:
        #         valid_count += counter[(num-k)]

        # return valid_count


        
        # difference = {}

        # # Counter
        # for num in nums:
        #     diff = abs(num - k)
        #     if diff not in difference:
        #         difference[diff] = 1
        #     else:
        #         difference[diff] += 1
        # print(difference)
        # # count valid pairs
        # count = 0
        # for num in nums:
        #     if num in difference:
        #         count += difference[num]

        # return count
