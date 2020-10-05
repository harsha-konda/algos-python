class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        result = [-1 for _ in nums]
        for i in range(2*len(nums)):
            while(stack and nums[stack[-1]] < nums[i%len(nums)]):
                ele = stack.pop()
                result[ele] = nums[i%len(nums)]
            stack.append(i%len(nums))
        return result

if __name__ == '__main__':
	assert(Solution().nextGreaterElements([1,2,3,2,1])==[2,3,-1,3,2])