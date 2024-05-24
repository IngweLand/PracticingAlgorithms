class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = 0
        print(*reversed(range(len(s))))
        for i in reversed(range(len(s))):
            if s[i] == ' ':
                continue
            for j in reversed(range(0, i + 1)):
                print(*reversed(range(0, i + 1)))
                if s[j] != ' ':
                    r += 1
                else:
                    return r
            break
        return r

if __name__ == "__main__":
# Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.lengthOfLastWord("day")