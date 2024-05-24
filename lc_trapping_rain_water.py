from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        width = len(height)
        
        if width < 3:
            return 0
        
        highest = max(height)
        total = highest*width
        total_mountains = sum(height)
        last_peak = height[0]
        for i in range(1, width):
            h = height[i]
            if h > last_peak:
                total -= (i * (h-last_peak))
                last_peak = h
            if last_peak == highest:
                break
        last_peak = height[width - 1]  
        for i in reversed(range(0, width - 1)):
            h = height[i]
            if h > last_peak:
                total -= ((width - i - 1) * (h-last_peak))
                last_peak = h
            if last_peak == highest:
                break  
        return total - total_mountains

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()
    print(solution_instance.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

