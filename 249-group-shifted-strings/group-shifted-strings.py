class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Input: List[str]
        Output: List[List[str]]
        Test Cases
            - ["abc","xyz","a","d"]
                [["abc","xyz"],["a","d"]]
            - ["abc"]
                [["abc"]]
        
        Constraints
            - 1 <= strings.length <=200
            - 1 <= strings[i].length <= 50
            - strings[i] consists of lower case english letters
        
        Assumptions
            - 
        """

        # Approach 1: Time O(strings.length * strings[i].length) Space O(strings.length * strings[i].length)
        # dict {tuple(ord(eachletter)) : []}
        groups = defaultdict(list)
        # iterate through the list
        for curr_s in strings:
            temp_tuple = []
            for ch in curr_s:
                ch_ord = ord(ch)-ord(curr_s[0])
                if ch_ord < 0:
                    ch_ord = ch_ord + 26
                temp_tuple.append(ch_ord)
            # Create tuple and append to dict
            # DEBUG print(f"{curr_s}:{temp_tuple}")
            groups[tuple(temp_tuple)].append(curr_s)
        
        # DEBUG print(groups)
        return list(groups.values())

        # Approach 2: Brute force


        
