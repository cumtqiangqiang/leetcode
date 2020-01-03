
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
from typing import List

def twoSum(nums: List[int], target: int):
    dic = {}
    index_list = []
    for i in range(len(nums)):
        num = nums[i]
        diff_num = target - num
        if num not in dic.keys():
            dic[diff_num] = i
        else:
            index_list.append(dic[num])
            index_list.append(i)

    return index_list




if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    list = twoSum(nums,17)
    print(list)