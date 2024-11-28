class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """
        given 2 arrays, return the product

        Test Case:
            [[1,3],[2,3]]  [[6,3],[3,3]] -> [6,6]
            [[1,3],[2,1],[3,2]] [[2,3],[3,1],[3,2]] -> [[2,3],[6,1],[9,2]]
        
        Constraints:
            1 <= len(encoded1), len(encoded2) <= 10^5 
            len(enoded1[i]) == 2
            len(enoded2[i]) == 2
            1 <= val, freq <= 10^4
        """

        q1 = deque(encoded1) # []
        q2 = deque(encoded2) # []
        res = []             # [[2,3], [6,1],[9,2]]

        while q1:
            # pop q1
            val1, f1 = q1.popleft()  # 3 , 2
            # pop q2
            val2, f2 = q2.popleft()  # 3 , 2

            if f1 > f2:
                # add new item to start of q1 [val1,f1-f2]
                q1.appendleft([val1,f1-f2])
                # set f1 = f2
                f1 = f2
            
            if f2 > f1:
                # add new item to start of q2 [val2,f2-f1]
                q2.appendleft([val2,f2-f1])
                f2 = f1 # <
            
            res.append([val1*val2, f1])

        # merge same vals
        final_res  = []
        res.append([None, None])
        if len(res) > 1:
            for i in range(1,len(res),1):
                # check if prev.val == curr.val
                if res[i-1][0] == res[i][0]:
                    # don't append curr
                    # update curr.freq = curr.freq + prev.freq
                    res[i][1] += res[i-1][1]
                else:
                    # append previous one
                    final_res.append(res[i-1])
                

        return final_res

        