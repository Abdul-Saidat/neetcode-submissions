class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
                else:
                    j += 1
            else:
                i += 1
        
        return res