# https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l, self.m = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if (val in self.m):
            return False

        self.l.append(val)
        self.m[val] = len(self.l) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        def swap(i, j):
            temp = self.l[i]
            val_i = self.l[i]
            val_j = self.l[j]

            self.l[i] = self.l[j]
            self.l[j] = temp

            self.m[val_i] = j
            self.m[val_j] = i

        if (val not in self.m):
            return False

        i = self.m[val]

        swap(i, len(self.l) - 1)
        self.l.pop()
        del self.m[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = randint(0, len(self.l) - 1)
        return self.l[i]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
