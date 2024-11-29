class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. 

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
# [[1,4],[4,5],[7,10],[8,11],[12,14]] -> [[1,5],[7,11],[12,14]]
# [[1,4],[4,5],[7,10],[8,11]] -> [[1,5],[7,11]]



# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104


# class Intervals:
    def merge(self, intervals:List[List[int]]) -> List[int]:
        #  [[1,3],[2,6],[8,10],[15,18]]

        # approach 1: Time O(n) Space O(1)
        if len(intervals) == 1:
            return intervals

        intervals.sort()

        # append an placeholder item in the list
        # intervals.append([105,105])
        prev_start,prev_end = intervals[0] # 15,18
        i = 1 # 4
        res = [] # [[1,6],[8,10],[15,18]]
        # iterate through each item, starting from second item
        while i < len(intervals): # < 4
            curr_start, curr_end = intervals[i] # 15,18
            if curr_start <= prev_end:
                # prev_start = min(curr_start, prev_start)
                prev_end = max(prev_end, curr_end)
            else:
                # append the prev_start and prev_end to result
                res.append([prev_start,prev_end])
                prev_start = curr_start
                prev_end = curr_end
            i += 1

        res.append([prev_start,prev_end])

        return res #[[1,6],[8,10],[15,18]]        
        
        
        
        
        # """
        # merge overlapping intervals. 

        # Test Cases
        #     [[1,3],[2,6],[4,5],[8,10],[15,18]] -> [[1,6][8,10],[15,18]]

        # Constraints
        #     1 <= len(intervals) <= 10000
        #     len(intervals[i]) == 2
        #     0 <= start_i, end_i <= 10000

        # """
        # # sort intervals on start
        # intervals.sort(key=lambda x: x[0])

        # # iterate left to right, keeping track of last_start last_end
        # res = []
        # last_start, last_end = intervals[0]
        # i = 1
        # intervals.append([10001,10001]) # since we are not processing last one
        # while i < len(intervals):
        #     curr_start, curr_end = intervals[i]
        #     if last_end >= curr_start: 
        #         # keep merging
        #         last_end = max(curr_end,last_end)
                
        #     else:
        #         res.append([last_start,last_end])
        #         last_start = curr_start
        #         last_end = curr_end

        #     i+=1

        # return res


        