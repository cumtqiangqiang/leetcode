
class Solution(object):

		def longestPalindrome(self,s: str) -> str:
			start = 0
			end = 0
			for i in range(len(s)):
				len1 = self.getTheLengthOfPalindrome(s,i,i)
				len2 = self.getTheLengthOfPalindrome(s,i,i+1)
				maxLen = max(len1,len2)
				if maxLen > end - start:
					start = i - (maxLen - 1)//2
					end = i + maxLen//2


			return s[start:end+1]


		def getTheLengthOfPalindrome(self,s,left,right):
			while(left >= 0 and right <= len(s) and s[left:left+1] == s[right:right+1]):
				left -= 1
				right += 1

			return right - left -1


