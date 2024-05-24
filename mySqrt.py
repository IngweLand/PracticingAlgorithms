class Solution:
    def mySqrt(self, x: int) -> int:
        g = x / 2.0  # Initial guess
        while True:
            g_new = 0.5 * (g + x / g)
            if g - g_new < 0.00001:
                break
            g = g_new
        print(int(g))
        print(g)
        return g

if __name__ == "__main__":
# Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.mySqrt(2147395599)