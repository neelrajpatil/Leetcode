class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # ## Approach 3:
        # s_dict = {}
        # t_dict = {}

        # for i in range(len(s)):
        #     s_dict[s[i]] = s_dict.get(s[i],0) + 1
        #     t_dict[t[i]] = t_dict.get(t[i],0) + 1
        
        # for char in s_dict:
        #     if s_dict.get(char,0) != t_dict.get(char,0):
        #         return False
        # return True

        ## Approach 2:
        if Counter(s) == Counter(t):
            return True
        return False

        # ## Approach 1: Count chars in one string, decrement from other string.
        # s_dict = dict() 
        # # single pass s
        # for i in range(len(s)):
        #     #make dict with char as  and count as value
        #     s_dict[s[i]] = 1 + s_dict.get(s[i],0)
        # print(s_dict)


        # # single pass t
        # for i in range(len(t)):
        #     # remove every char from dict, if not in dict return false
        #     if s_dict.get(t[i],0) == 0:
        #         return False
        #     s_dict[t[i]] = s_dict.get(t[i],0) - 1

        
        # # if dict is empty
        # if set(s_dict.values())== set([0]):
        #     return True
        # return False

        