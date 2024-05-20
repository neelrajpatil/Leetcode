class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Approach 2 O(m*n)
        res = defaultdict(list)
        for word in strs:
            chars = [0]*26
            for char in word:
                chars[ord(char)-ord('a')] += 1
            res[tuple(chars)].append(word)

        return res.values()

        
        # # Approach 1 O(m*n*log n)
        # all_sets = {}
        # for word in strs:
        #     curr_set = tuple(sorted(word))
        #     if curr_set in all_sets.keys():
        #         all_sets[curr_set].append(word)
        #     else:
        #         all_sets[curr_set] = [word]
        # return all_sets.values()