# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List 

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newList = []
        currentSum = 0

        for num in nums:
            currentSum += num
            newList.append(currentSum)

        return newList
