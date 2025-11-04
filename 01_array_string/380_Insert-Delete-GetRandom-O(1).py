import random

class RandomizedSet:

    def __init__(self):

        self.dic = {}
        self.set = []
        
    def insert(self, val: int) -> bool:

        if val in self.set:
            return False

        self.set.append(val)
        self.dic[val] = len(self.set) - 1

        return True

    # 여기서 list.remove()를 쓰면 안됨 -> O(n)이 되기 때문
    def remove(self, val: int) -> bool:

        if val not in self.set:
            return False

        remove_idx = self.dic[val]
        last_val = self.set[-1]

        self.set[remove_idx] = last_val
        self.dic[last_val] = remove_idx

        self.set.pop()
        del self.dic[val]
        
        return True
    
    def getRandom(self) -> int:

        return random.choice(self.set)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
