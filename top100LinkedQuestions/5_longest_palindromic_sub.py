'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''

def longestPalindrome(s: str) -> str:
	start = 0
	end = 0
	for i in range(len(s)):
		len1 = getTheLengthOfPalindrome(s,i,i)
		len2 = getTheLengthOfPalindrome(s,i,i+1)
		maxLen = max(len1,len2)
		if maxLen > end - start:
			start = i - (maxLen - 1)//2
			end = i + maxLen//2


	return s[start:end+1]


def getTheLengthOfPalindrome(s,left,right):
	while(left >= 0 and right <= len(s) and s[left:left+1] == s[right:right+1]):
		left -= 1
		right += 1

	return right - left -1
if __name__ == '__main__':
	s = longestPalindrome("acbbcd")
	print(s)