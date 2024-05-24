from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            n = digits[i] + 1
            if n == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    break
            else:
                digits[i] = n
                break
        return digits
