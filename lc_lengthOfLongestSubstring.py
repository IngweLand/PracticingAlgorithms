class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len == 0:
            return 0
        elif s_len == 1:
            return 1
        elif s_len == 2:
            if s[0] == s[1]:
                return 1
            else: 
                return 2
        hashtable = {}
        m = 0
        start = 0
        for idx, char in enumerate(s):
            if char in hashtable:
                prev = hashtable[char]
                if prev < start:
                    m = max(m, idx - max(prev, start - 1))
                start = max(start, prev + 1)
            else:
                m = max(m, idx - start + 1)
            hashtable[char] = idx
        return m
    

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()
    s = "abba"
    # s = "abcabcbb"
    s = "loddktdji"
    # s = "aabaab!bb"
    # s = "dvdf"
    # s = "au"
    print(solution_instance.lengthOfLongestSubstring(s))
