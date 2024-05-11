class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ## Approach 1: 
        s_dict = dict() 
        # single pass s
        for i in range(len(s)):
            #make dict with char as  and count as value
            s_dict[s[i]] = 1 + s_dict.get(s[i],0)
        print(s_dict)


        # single pass t
        for i in range(len(t)):
            # remove every char from dict, if not in dict return false
            if s_dict.get(t[i],0) == 0:
                return False
            s_dict[t[i]] = s_dict.get(t[i],0) - 1

        
        # if dict is empty
        if set(s_dict.values())== set([0]):
            return True
        return False

        