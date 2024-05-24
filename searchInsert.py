from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if nums[0] >= target:
            return 0
        elif nums[l - 1] < target:
            return l
        min = 0
        max = l
        i = int(l / 2)
        while int(i / 2) > 0:
            if nums[i] == target:
                return i
            if nums[i] > target:
                max = i
                i = int(i / 2)
            else:
                i = i + int(i / 2)
        if nums[i] < target:
            return i + 1
        return i

if __name__ == "__main__":
# Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.searchInsert([1,3,5], 2)
