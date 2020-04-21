from typing import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		i = 0
		length = len(nums)
		if length == 0:return 0
		while i< len(nums) and len(nums) > 1:
			if (nums[i-1] == nums[i]):
				nums.pop(i)
			else:
				i+=1
		return len(nums)



if __name__ == '__main__':
	s = Solution()
	nums = [1]
	len = s.removeDuplicates(nums)
	print(len)