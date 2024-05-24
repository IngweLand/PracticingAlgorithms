class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        if n == 4:
            return 5
        sum = n
        isEven = n % 2 == 0
        j = int(n / 2) - 1
        if not isEven:
            sum += j * (j + 1)
        else:
            sum += j ** 2

        return int(sum)

if __name__ == "__main__":
# Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.climbStairs(5)