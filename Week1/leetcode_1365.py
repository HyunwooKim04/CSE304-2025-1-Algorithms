# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        result = [0] * len(nums)

        for i in range(len(nums)):
            if i > 0 and sorted_nums[i][0] > sorted_nums[i-1][0]:
                result[sorted_nums[i][1]] = i
        
        return result
