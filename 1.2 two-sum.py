def twoSumHashing(num_arr, pair_sum):
    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            index = hashTable.get(complement)
            print("Pair with sum", pair_sum,"is: (", i,",", index,")")
        hashTable[num_arr[i]] = i

# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 9    
  
# Calling function
twoSumHashing(num_arr, pair_sum)


# Leetcode:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashTable = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashTable:
#                 index = hashTable.get(complement)
#                 # print("Pair with sum", target,"is: (", i,",", index,")")
#                 return [i, index]
#             hashTable[nums[i]] = i

# Runtime: 40 ms, faster than 94.97% of Python3 online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 11.57% of Python3 online submissions for Two Sum.