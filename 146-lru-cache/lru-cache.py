class Node:
    def __init__(self, key, val,prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    """

    Test Case:              |
        ["LRUCache","put","put","get","put","get","put","get","get","get"]
        [[2],       [1,1],[2,2],[1],  [3,3],[2],   [4,4],[1],   [3],[4]]


    constraints:
        1 <= cap <= 3000
        0 <= key <= 10000
        0 <= value <= 100000
        at most 2*10^5 calls to put and get

    """


    def __init__(self, capacity: int):
        # dict
        self.cache = {} # {key:Node} {1:Node(1,1,start,end),2:Node(1,1,None,None)}
        # doubly linked list
        self.start = Node(0,0)  # start -> Node(1,1) -> end
        self.end = Node(0,0)    # start <- Node(1,1) <- end
        self.start.next = self.end
        self.end.prev = self.start
        # capacity
        self.capacity = capacity # 2
        

    def get(self, key: int) -> int:
        """
        Time O(n)

        returns -1 if not found else returns value
        """
        if key not in self.cache.keys():
            return -1
        
        # fetch value
        node = self.cache[key]
        # change its order in doubly linked list
        # In Q, remove from current spot
        self._remove_from_q(key)
        # In Q, add to rightmost spot
        self._add_to_q(key)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        """
        Time O(n)
        """

        # if key exists
        if key in self.cache.keys():
            # update the value of key 
            node = self.cache[key] 
            node.val = value
            # change its order in doubly linked list
            self._remove_from_q(key)
            self._add_to_q(key)
            return

        # if capacity exceeded
        if self.capacity == len(self.cache.keys()):
            # evict LRU
            # find LRU
            LRU_node = self.start.next
            # remove_from_q
            self._remove_from_q(LRU_node.key)
            # remove from dict
            del self.cache[LRU_node.key]

        
        # add key value to dict
        new_node = Node(key,value)
        self.cache[key] = new_node
        # add to doubly linked list
        self._add_to_q(key)
        return
    
    def _remove_from_q(self, key:int) -> None:
        if key not in self.cache.keys():
            print("key not present when trying to remove from q")
            return
        
        node = self.cache[key]
        # connect prev and next node
        node.prev.next = node.next
        node.next.prev = node.prev
        # reset curr_node pointers to None
        node.next = None
        node.prev = None
        return
    
    def _add_to_q(self, key:int) -> None:
        """
        assuming key always exists. Assuming the node is dangling
        """
        node = self.cache[key]
        last_node = self.end
        second_last_node = self.end.prev

        second_last_node.next = node
        last_node.prev = node
        node.prev = second_last_node
        node.next = last_node
        return



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)