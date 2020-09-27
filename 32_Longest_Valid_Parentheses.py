# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
	def longestValidParentheses(self,s):
		stack,count,maxCount  = [],0,0

		stack = [(-1,count)]
		for i in range(len(s)):
			ch = s[i]
			if ch == '(':
				stack.append((i,count))
				count+=1
				continue

			if stack and count >0:
				count-=1
				j,prevCount = stack.pop()
				
				if count == prevCount:
					maxCount = max(i-stack[-1][0],maxCount)

			else: 
				stack = [(i,0)]

		return maxCount

if __name__ == '__main__':
	assert(Solution().longestValidParentheses(")()())")==4)
	assert(Solution().longestValidParentheses("(()()")==4)


