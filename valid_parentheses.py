class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l == 1:
            return False
        a = [s[0]]
        for i in range(1, l):
            str = s[i]
            if str not in pairs:
                a.append(str)
            elif len(a) == 0:
                return False
            elif pairs[s[i]] == a[len(a) - 1]:
                a.pop()
            else:
                return False
        return len(a) == 0

pairs = {
    ')':'(',
    '}':'{',
    ']':'['
}

if __name__ == "__main__":
# Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.isValid("()[]{}")