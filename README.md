# algos-python

## Tips
- Always create examples
    - use the naive appoach
    - recognize patterns in the problem

- If it is a maximzation or a minimization problem , 
list all the different permuations for the problem 
and eliminate duplicates


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