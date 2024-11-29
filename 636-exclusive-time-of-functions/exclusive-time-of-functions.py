class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        returns a list with the exclusiveTime of ith function in ith postion

        Test Cases
            2 ["0:start:0","1:start:2","1:end:5","0:end:6"] -> [3,4,]

            1 ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"] -> 

        Constraints
            1 <= logs.length <= 500
            1 <= function_id < n <= 100
            0 <= timestamp <= 10^9
            
        """

        # Approach 1:

        stack = []  #[function_id] [0]
        res = [0 for i in range(n)] #[2]

        now = 0 # 0
        prev = 0 # 0
        prev_id = None #0
        prev_event = None #'start'

        # iterate through the list
        for log in logs: # "0:start:2"
            # get function_id, event, timestamp(now)
            function_id,event,now = log.split(':') # 0, start, 2
            function_id = int(function_id) # 0
            now = int(now) # 2

            
            if event == 'end':
                # ensure funcition_id == top of the stack function_id
                if function_id != stack[-1]:
                    print(f"Error in handling stack. stack: \n{stack}")
                
                time_executed = now - prev + 1 #since it is inclusive
                res[function_id] += time_executed
                # pop stack
                stack.pop()
                prev = now + 1

            else: # event is start
                # if stack not empty
                if stack:
                    # stop whatever previous event was running
                    last_running_id = stack[-1] #0
                    time_executed = now - prev # 
                    res[last_running_id] += time_executed
                # push to stack[function_id]
                stack.append(function_id)
                prev = now

            prev_id = function_id
            prev_event = event

        return res
