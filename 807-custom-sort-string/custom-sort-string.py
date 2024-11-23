class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Approach 1 reattempted
        # Create a mapping for the order
        order_mapping = {o: i for i, o in enumerate(order)}  # Map each char to its position in `order`
        order_set = set(order)  # To check membership in `order`

        # Count the occurrences of each character in `s`
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        # Separate characters into two groups: those in `order` and those not in `order`
        in_order = []
        not_in_order = []

        for c in s:
            if c in order_set:
                in_order.append(c)
            else:
                not_in_order.append(c)

        # Sort characters in `in_order` based on their order in `order`
        in_order.sort(key=lambda x: order_mapping[x])

        # Append the characters that are not in `order` to the end
        result = ''.join(in_order) + ''.join(not_in_order)
        return result
        # # Approach 2
        # res = []
        # count = defaultdict(int)
        # for c in s:
        #     count[c] += 1
        


        # for char in order:
        #     res.extend([char]*count[char])
        #     del count[char]
        
        # for char,ct in count.items():
        #     res.extend([char]*count[char])
        
        # return "".join(res)

        # # Approach 1
        # # # order_mapping
        # # order_mapping = defaultdict(int) # {1:'a',2:'b'} 
        # # order_set = set(order)
        # # for i, o in enumerate(order):
        # #     order_mapping[i+1] = o
        
        # # counter = defaultdict(int) # {'a':12,'b':2}
        # # no_order = []
        # # for c in s:
        # #     counter[c] += 1
        # #     if c not in order_set:
        # #         no_order.append(c)


        # # res = []

        # # for i in range(len(order)):
        # #     curr_char = order_mapping[i]
        # #     res.append(curr_char*counter[curr_char])

        # # res = res + no_order

        # # return res
        


            
        