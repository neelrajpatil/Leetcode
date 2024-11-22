class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        curr = ""

        for c in path+'/':
            if c == '/':
                if curr == '..':
                    if stack: stack.pop()
                elif curr != "." and curr!= "":
                    stack.append(curr)
                curr = ""
            else:
                curr += c

        return '/' + '/'.join(stack)





        # stack = []

        # # iterate thru each char
        # i = 0
        # curr_dir_file = ''
        # while i < len(path):

        #     # if it is . then check next 2 chars
        #     if path[i] == '.':
                
        #         if i+1 >= len(path) or path[i+1] == '/': # if it is .  
        #             i += 1
        #             continue   
        #         elif path[i+1] == '.' and (i+2 >= len(path) or path[i+2] == '/'): # if it is ..
        #             if stack:
        #                 stack.pop() # pop from stack
        #             i += 2
        #             continue
        #     # if it is /
        #     if path[i] == '/':
        #         i += 1
        #         continue
        #     else:
        #         while i < len(path) and path[i] != '/':
        #             curr_dir_file += path[i]
        #             i+=1
        #         stack.append(curr_dir_file)
        #         curr_dir_file = ''
        
        
        # return '/'.join(['']+stack) if stack else '/'

                
