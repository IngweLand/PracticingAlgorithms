from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        shortest = min(strs)
        first = strs[0]
        if shortest == first:
            return first
        result = ''
        for i, char in enumerate(shortest):
            if char == first[i]:
                result += char
            else:
                break
        return result
        pass


if __name__ == "__main__":
# Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.longestCommonPrefix(["flower","flow","flight"])
