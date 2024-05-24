from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []

# To instantiate the class and call the method
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()

    # Example list of numbers and target
    # nums_example = [2, 7, 11, 15]
    # target_example = 9
    # nums_example = [3,2,4]
    # target_example = 6
    nums_example = [3,2,3]
    target_example = 6
    
    # Call the twoSum method
    result = solution_instance.twoSum(nums_example, target_example)
    
    # Print the result
    print(result)
