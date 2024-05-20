class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_sets = {}
        for word in strs:
            curr_set = tuple(sorted(word))
            if curr_set in all_sets.keys():
                all_sets[curr_set].append(word)
            else:
                all_sets[curr_set] = [word]
        
        return all_sets.values()
