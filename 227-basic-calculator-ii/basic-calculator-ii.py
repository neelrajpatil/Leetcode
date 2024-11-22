class Solution:
    def calculate(self, s: str) -> int:
        # s = "3+2*2"
        stack = [] # [3,]

        i = 0 # 2
        curr_op = '' # '+'
        curr_num = 0
        while i < len(s): # iterate thru chars # 1 < 5
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
                curr_op = s[i]
            else: # if digit
                # get all digits into curr_num
                while i < len(s) and s[i].isdigit(): #
                    curr_num = curr_num*10 + int(s[i]) # 3
                    i += 1 
                i -= 1

                if curr_op == '/' :
                    # pop from stack and perform operation, storing result in curr_num
                    temp_num = stack.pop()
                    res = int(temp_num/curr_num)
                    stack.append(res)
                    curr_num = 0

                elif curr_op == '*':
                    temp_num = stack.pop()
                    res = int(curr_num * temp_num)
                    stack.append(res)
                    curr_num = 0
                elif  curr_op == '-':
                    stack.append(-curr_num)
                    curr_num = 0
                else:
                    stack.append(curr_num)
                    curr_num = 0
            i += 1
        
        return sum(stack)
            
                
        




















        # iterate thru chars

            # if digit
                # get all digits iznto curr_number
                # if curr_operation is * or / 
                    # pop from stack and / or * with curr_number
                    # store ans in curr_number
                # elif curr_operation is - 
                    # set curr_number to - curr_number
                # add curr_number to stack
            
            # if char
                # set curr_operation to char 

        