class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}

      for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
        # i = 0
        # res = []
        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             res.append(i)
        #             res.append(j)
        #             return res
        #         else:
        #             j += 1
                
        #     i += 1
        
        # return res

