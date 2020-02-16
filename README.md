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

## To do 
- sorted matrix problems
