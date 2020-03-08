'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from typing import List

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		dic = {}
		result = set()
		for i,num1 in enumerate(nums):
			for j in range(1,len(nums)):
				num2 = nums[j]
				d_num  = -num1 - num2
				if num2 not in dic.keys():
					dic[d_num] = j
				else:
					result.add((num1,num2,d_num))
		return list(result)

	def threeSum1(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		result = []
		for i in range(len(nums) - 2):
			if nums[i] > 0 : break
			if i > 0 and nums[i] == nums[i-1]:continue
			j = i+1
			k = len(nums) - 1
			# [-2, 0, 1, 1,1, 2]
			while j < k:
				if nums[i] + nums[j] + nums[k] == 0:
					result.append([nums[i],nums[j],nums[k]])
					j+=1
					k-=1
					while nums[j] == nums[j-1] and j < k:j += 1
					while nums[k] == nums[k+1] and j < k: k -= 1
				elif nums[i] + nums[j] + nums[k] < 0:
					j += 1
					while nums[j] == nums[j-1] and j < k :j+=1
				else:
					k -=1
					while nums[k] == nums[k+1] and j < k: k-=1

		return  result






if __name__ == '__main__':
	s = Solution()
	# a = s.threeSum([-1, 0, 1, 2, -1, -4])
	b = s.threeSum1([-2,0,1,1,1,1,2])
	print(b)