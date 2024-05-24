class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        values = {1, n}
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                values.add(i)          
                values.add(n // i)      
        values = sorted(values)
        if len(values) >= k:
            return values[k-1]
        return -1
    
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.kthFactor(100000000, 4)


