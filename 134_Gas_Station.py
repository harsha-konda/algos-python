# https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i, j = 0, 0
        fuel = 0
        reset = True
        hasPassed = False

        while (not (reset and hasPassed)):
            print(i, j)
            if (i == j and not reset):
                return i
            fuel = fuel + gas[j] - cost[j]
            j += 1

            if (j >= len(gas)):
                hasPassed = True

            j = j % len(gas)

            if (fuel < 0):
                i = j
                fuel = 0
                reset = True
            else:
                reset = False
        return -1
