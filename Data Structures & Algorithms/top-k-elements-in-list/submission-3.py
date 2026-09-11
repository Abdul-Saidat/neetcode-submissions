class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1, 2, 2, 3, 3, 3
        frequency = {}
        result = []
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        
        sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        # print(sorted_frequency)

        k_values = sorted_frequency[:k]
        # print(k_values)

        for num in k_values:
            result.append(num[0])
        
        return result