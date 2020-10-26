class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        left = [-1 for _ in A]
        stack = []
        for i in range(len(A)):
            while(stack and A[stack[-1]] > A[i]):
                stack.pop()            
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        right = [len(A) for _ in A]
        stack = []
        for i in range(len(A)): 
            while(stack and A[stack[-1]] > A[i]):
                ele = stack.pop()
                right[ele] = i    
            stack.append(i)
        result = 0
        for i in range(len(A)):
            result = (result + A[i]*(right[i] - i)*(i-left[i])) % (10**9+7)
            
        return result 