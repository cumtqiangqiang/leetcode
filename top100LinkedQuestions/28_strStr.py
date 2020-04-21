'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''
class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		res = -1
		i = 0
		j = len(needle)
		if not needle : return 0
		if len(needle) > len(haystack)  : return  res
		while i <  len(haystack):
			if haystack[i] == needle:
				res = i
				break
			if haystack[i:j] == needle:
				res = i
				break
			i += 1
			j += 1
		return res




if __name__ == '__main__':
	s = Solution()
	res = s.strStr("","")

	print(res)

