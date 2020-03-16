'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution:
	def isValid(self, s: str) -> bool:
		length = len(s)
		d1 = {'[': ']', '{': '}', '(': ')'}
		if length % 2 != 0: return False
		for i, ss in enumerate(s):
			print(ss)

		return False


class Solution1:
	def isValid(self, s: str) -> bool:
		parentheses = {'{': '}', '[': ']', '(': ')'}
		stack = []
		for _ in s:
			if _ in parentheses:
				stack += parentheses.get(_),
			elif not stack or stack.pop() != _:
				return False
		return not stack


if __name__ == '__main__':
	s = Solution1()
	a = s.isValid('[()]')
	print(a)
