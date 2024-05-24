class Solution:
    def partitionString(self, s: str) -> int:
        if s.count == 1:
            return 1
        hashtable = {}
        result = 0
        for idx, char in enumerate(s):
            if char in hashtable:
                result += 1
                hashtable = {}
            hashtable[char] = idx
        return result + 1

# s = "abacaba"
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()
    s = "hdklqkcssgxlvehva"
    print(solution_instance.partitionString(s))