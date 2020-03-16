from typing import List


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		if not digits:return []
		d = [' ','*','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
		res = []

		def dfs(temp,indx):
			if indx == len(digits):
				res.append(temp)
				return
			c = digits[indx]
			# letters = d[ord(c) - 48]
			letters = d[int(c)]
			for i in letters:
				dfs(temp+i,indx + 1)

		dfs('',0)

		return  res

	def letterCombinations1(self, digits: str) -> List[str]:
		if not digits:return []
		d = [' ','*','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
		result = [""]
		for i in  digits:
			size = len(result)
			letters = d[int(i)]

			for j in range(size):
				temp = result.pop(0)
				for k in letters:
					result.append(temp+k)
		return  result



if __name__ == '__main__':
	s = Solution()
	# a = s.letterCombinations('234')
	b = s.letterCombinations1('234')
	print(b)