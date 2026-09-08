class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let seen = new Set()

        for (let i = 0; i < nums.length; i++) {
           if (seen.has(nums[i])) {
            return true
           } else {
            seen.add(nums[i])
           }
        }
            return false
    }
}
// for i in nums:
//         if numCount == i:
//             count += 1
//         if count >= 1:
//             return True
//         else:
//             return False
