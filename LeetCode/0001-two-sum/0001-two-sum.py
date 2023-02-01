class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# using dictionary 3800ms -> 75ms
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_dict = {}
#         for i, num in enumerate(nums):
#             if target - num in nums_dict:
#                 return [nums_dict[target - num], i]
#             nums_dict[num] = i