"""
@author : Gargi Kshirsagar
@Problem statement : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
@Difficulty : Easy
@Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if num[j] == target - nums[i]:
                    return [i, j]


num = []
n = int(input("nums ="))
for i in range(0, n):
    ele = int(input())
    num.append(ele)

int(input("target ="))
