class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        i = 0
        result = 0
        while i < l:

            if (i < l - 1):
                ss = s[i:i + 2]
                if ss in roman_dict:
                    result += roman_dict[ss]
                    i += 2
                    continue
            if s[i] in roman_dict:
                result += roman_dict[s[i]]
            i += 1
        return result


roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.romanToInt("MCMXCIV")
