from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 1
        i, j = 1, 1
        while i < l:
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

if __name__ == "__main__":
# Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.removeDuplicates([1, 1, 1, 1, 2, 3])


