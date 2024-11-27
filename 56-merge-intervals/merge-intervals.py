class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        merge overlapping intervals. 

        Test Cases
            [[1,3],[2,6],[4,5],[8,10],[15,18]] -> [[1,6][8,10],[15,18]]

        Constraints
            1 <= len(intervals) <= 10000
            len(intervals[i]) == 2
            0 <= start_i, end_i <= 10000

        """
        # sort intervals on start
        intervals.sort(key=lambda x: x[0])

        # iterate left to right, keeping track of last_start last_end
        res = []
        last_start, last_end = intervals[0]
        i = 1
        intervals.append([10001,10001]) # since we are not processing last one
        while i < len(intervals):
            curr_start, curr_end = intervals[i]
            if last_end >= curr_start: 
                # keep merging
                last_end = max(curr_end,last_end)
                
            else:
                res.append([last_start,last_end])
                last_start = curr_start
                last_end = curr_end

            i+=1

        return res


        