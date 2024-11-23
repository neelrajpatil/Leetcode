class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        


        for char in order:
            res.extend([char]*count[char])
            del count[char]
        
        for char,ct in count.items():
            res.extend([char]*count[char])
        
        return "".join(res)

        # # order_mapping
        # order_mapping = defaultdict(int) # {1:'a',2:'b'} 
        # order_set = set(order)
        # for i, o in enumerate(order):
        #     order_mapping[i+1] = o
        
        # counter = defaultdict(int) # {'a':12,'b':2}
        # no_order = []
        # for c in s:
        #     counter[c] += 1
        #     if c not in order_set:
        #         no_order.append(c)


        # res = []

        # for i in range(len(order)):
        #     curr_char = order_mapping[i]
        #     res.append(curr_char*counter[curr_char])

        # res = res + no_order

        # return res
        


            
        