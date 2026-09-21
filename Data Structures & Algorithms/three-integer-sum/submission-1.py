class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        result = []

        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)

                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            i += 1

        return result























        # i = 0 
        # result = []

        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         k = j + 1
        #         while k < len(nums):
        #             sum = nums[i] + nums[j] + nums[k]
        #             if sum == 0:
        #                 triplet = [nums[i], nums[j], nums[k]]
        #                 triplet.sort()
        #                 if triplet not in result:
        #                     result.append(triplet)
        #             k += 1
        #         j += 1
        #     i += 1

        # return result