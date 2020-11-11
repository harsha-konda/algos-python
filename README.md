# algos-python

## Tips
- Always create examples
    - use the naive appoach
    - recognize patterns in the problem

- If it is a maximzation or a minimization problem , 
list all the different permuations for the problem 
and eliminate duplicates

## Generalized approach for solving problem
1. Come up with brute force solution
2. Think of a simpler version of the problem
3. Think about problem using simple examples -> try noticing pattern
4. use some visualization


## Python libraries

### Heapq

```python
from heapq import *
h = []
# pushes on to a heap 
heappush(h, (5, 'write code'))

# pops minima from a heap
heappop(h)

# pushes and pops an ele
heappushpop(h, (3, 'drink'))

# transforms given list into heap
l = [1,2,3]
heapify(l)
```

## queue
```python
from collections import deque
q =  deque()

q.append('j') 
q.appendleft('k')
q.pop()      
q.popleft()      
```

## iter
```python
from itertools import *

i = iter([1,2,3])
next(i)
next(i)
next(i)
```

## Dynamic Programming
- Divide and Conquer
  - Break
  - Merge
  - Base Case
- DP in some cases is an optmization to the Divide and Conquer Subproblems. Usually, it reduces the O(x^y) to polynomial time
- Types of DP Problems:
  - Optimization problem: find the maximum, minimum of a problem space
  - Counting Problems: Number of permutations

## To do 
- sorted matrix problems
- using while loops 
- reasoning whether a problem is dp or not
- https://leetcode.com/problems/subarray-sum-equals-k/
- [coin-change-2](https://leetcode.com/problems/coin-change-2/)
- [critical-connections-in-network](https://leetcode.com/problems/critical-connections-in-a-network/ )
    -  why do you need to intialize `newRank =  rank`
- https://leetcode.com/problems/sum-of-subarray-minimums/
- https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
- https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU

## To do
- exact matching,fuzzy matching,
- get,set,delete,undo,redo
- gain,deadline -> schedule them to optimize for profit
- insert,delete,getRandom,getLast,get
- consistent hashing implementation
