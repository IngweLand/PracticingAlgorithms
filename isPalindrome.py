class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x < 10:
            return True

        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":
# Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.isPalindrome(10)