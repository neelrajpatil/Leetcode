class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        maximise num, by doing a single digit swap

        Test Cases:
            2736 -> 7236
            9973 -> 9973

        Constraints:
            0 <= num <= 10^8
        """
        if num < 10:
            return num
        
        # # Approach 1: Two Pointers
        # num_s = str(num)

        # position_idx  = None
        # digit_idx = None

        # left = 0 # index in string
        # right = len(num_s-1) # index in string

        # while left < right:


        # # Approach 2:
        # # 115

        # num_s = str(num) # 115
        # curr = 0 # 0
        # position_idx = None # None
        # digit_idx = None # None

        # # pass from left to right
        # while curr < len(num_s)-1: # < 2

        #     # find highest position to swap
        #     if int(num_s[curr]) < int(num_s[curr+1]): 
        #         position_idx = curr 
        #         digit_idx = curr+1
        #         curr += 2
        #         break
            
        #     curr += 1
        
        # if position_idx == None: # if everything is in descending order
        #     return num

        # # continue pass to find number to swap it with
        # while curr < len(num_s):
        #     if int(num_s[curr]) > int(num_s[digit_idx]):
        #         digit_idx = curr
        #     curr += 1
        
        # # make the swap
        # num_l = list(num_s)
        # num_l[position_idx],num_l[digit_idx] = num_l[digit_idx],num_l[position_idx]

        # return int("".join(num_l))


        # Approach 3: 2 passes. 
        if num < 10:
            return num

        num_l = list(str(num))
        # 1st pass, right to left, create a list of maxInRight and maxInRightIdx
        curr = len(num_l) - 1
        # start with rightmost number 
        maxInRight = {curr: [int(num_l[curr]),curr]} #{ currIndex: [maxInRightVal,maxInRightIdx]}
        curr -= 1
        while curr > -1:
            if int(num_l[curr]) > int(maxInRight[curr+1][0]):
                maxInRight[curr] = [int(num_l[curr]), curr]
            else:
                maxInRight[curr] = maxInRight[curr+1]
            curr -= 1


        # 2nd pass, left to right, 
        curr = 0 
        while curr < len(num_l):
            if int(num_l[curr]) < int(maxInRight[curr][0]):            
                # swap
                num_l[curr], num_l[maxInRight[curr][1]] = num_l[maxInRight[curr][1]], num_l[curr]
                break
            curr += 1

        return int("".join(num_l))









