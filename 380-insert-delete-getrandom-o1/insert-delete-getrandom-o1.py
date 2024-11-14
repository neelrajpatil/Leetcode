import random
class RandomizedSet:

    def __init__(self):
        self.arr = [] # 10,30
        self.map = {} # 10:0 , 30:1
        return
    
    def insert(self, val: int) -> bool:
        if val in self.map.keys():
            return False
        self.arr.append(val)
        self.map[val] = len(self.arr)-1
        return True
            

    def remove(self, val: int) -> bool: #20
        if val not in self.map.keys(): 
            return False
        # curr_element
        curr_pos = self.map[val] #1
        

        # last_element
        last_val = self.arr[-1] #30
        self.arr[curr_pos] = last_val 
        self.map[last_val] = curr_pos
        self.arr.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr) 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()