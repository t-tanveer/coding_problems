from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(len(nums)):
                # print("adding ", nums[x], " + ", nums[y] )
                if (nums[x]+nums[y] == target and x != y):
                    return [x,y]

driver = Solution()
print(driver.twoSum( [2,7,11,15], 9))
# Runtime: 48 ms, faster than 61.33% of Python3 online submissions for Two Sum.
# Memory Usage: 14.4 MB, less than 73.40% of Python3 online submissions for Two Sum.