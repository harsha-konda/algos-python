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

## To do 
- sorted matrix problems
- using while loops 
- reasoning whether a problem is dp or not
- https://leetcode.com/problems/subarray-sum-equals-k/
- [coin-change-2](https://leetcode.com/problems/coin-change-2/)
- [critical-connections-in-network](https://leetcode.com/problems/critical-connections-in-a-network/ )
    -  why do you need to intialize `newRank =  rank`