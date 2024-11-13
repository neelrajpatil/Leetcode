class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        check if words are in lexicographic order based on parsed order

        Test Cases
            - words = ["apple","app"], order = [abc...] ->  false

        Constraints
            - 1 <= words.length <= 100
            - 1 <= words[i].length <= 20
            - order.length == 26
            all chars in words and order are in lowercase english letters

        """

        # Apporoach 1
        # Dict mapping char to Order index
        # words = ["apple","app"], order = [abc...] ->  false
        # ["hello","leetcode"] "hlabcdefgijkmnopqrstuvwxyz"
        charOrder = {c:i for i,c in enumerate(order)}

        # Iterate thru pairs of words
        for i in range(len(words)-1): # 0
            l_word = words[i] # hello
            r_word = words[i+1] # leetcode
                                #5
            for j in range(len(l_word)): # 0
                # Handle edge case #1
                if len(r_word)-1 < j: 
                    return False

                if l_word[j] != r_word[j]: # find diff chars
                                #0                  #1
                    if charOrder[l_word[j]] > charOrder[r_word[j]]: # Check if both are not in order
                        return False
                    break

        return True
        
         