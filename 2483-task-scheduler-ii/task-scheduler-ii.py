class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        """
        return mimimum number of days needed to complete all tasks with spaces between same tasks
        
        Constraints
            1 <= tasks.length <= 10^5
            0 < tasks[i] <= 10^9
            1 <= space <= tasks.length

        Test cases
            [1,2,1,2,3,1] space=3 -> 9
        """

        # # Approach 1:
        # # [1,2,1,2,3,1] space=3 -> 9
        
        # # dict to store this
        # last_executed = {} #{task:last_executed_iteration_val} # {1:1,2:2,}
        # day_count = 0 # 3
        # curr_pointer = 0 # 2

        # #iterate until curr_pointer == len(tasks) - 1
        # while curr_pointer < len(tasks): # 2 < 6
        #     day_count += 1
        #     curr_task = tasks[curr_pointer] # 1
        #     if curr_task not in last_executed: 
        #         last_executed[curr_task] = day_count
        #         curr_pointer += 1
        #     # if currTask is NOT blocked by space using last_executed
        #     elif day_count-last_executed[curr_task] > space:
        #         last_executed[curr_task] = day_count
        #         curr_pointer += 1

        # return day_count

        # # Approach 2

        # # dict to store this
        # last_executed = {} #{task:last_executed_iteration_val} # {1:1,2:2,}
        # day_count = 0 # 3
        # curr_pointer = 0 # 2

        # #iterate until curr_pointer == len(tasks) - 1
        # while curr_pointer < len(tasks): # 2 < 6
        #     day_count += 1
        #     curr_task = tasks[curr_pointer] # 1
        #     if curr_task not in last_executed: 
        #         last_executed[curr_task] = day_count
        #         curr_pointer += 1
        #     # if currTask is NOT blocked by space using last_executed
        #     elif day_count-last_executed[curr_task] > space:
        #         last_executed[curr_task] = day_count
        #         curr_pointer += 1
        #     else:
        #         days_left = space - (day_count - last_executed[curr_task])
        #         day_count += days_left
        #         last_executed[curr_task] = day_count
        #         curr_pointer += 1

        # return day_count

        last_executed = {}  # Stores the last day a task was executed
        day_count = 0  # Keeps track of the current day

        for task in tasks:
            day_count += 1  # Assume we are completing a task on this day
            
            # If the task was executed before and the gap is less than space
            if task in last_executed and day_count - last_executed[task] <= space:
                # Jump to the next available day
                day_count = last_executed[task] + space + 1
            
            # Update the last executed day for the current task
            last_executed[task] = day_count

        return day_count