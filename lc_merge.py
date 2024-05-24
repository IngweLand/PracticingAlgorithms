from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l_len = len(ratings)
        if l_len == 1:
            return 1
        result = [1]*l_len
        i = 1
        while i < l_len:
            if ratings[i] > ratings[i-1]:
                result[i] = result[i - 1] + 1
            elif ratings[i] < ratings[i-1] and result[i] >= result[i-1]:
                result[i - 1] = result[i] + 1
                if (i < l_len - 1 and ratings[i + 1] >= ratings[i]) or (i == l_len - 1 and ratings[i] < ratings[i - 1]):
                    j = i
                    while j > 1:
                        if ratings[j - 1] < ratings[j - 2] and result[j - 1] >= result[j -2]:
                            result[j - 2] = result[j - 1] + 1
                            j -= 1
                        else:
                            break
            i += 1
        return sum(result)
    
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()
    print(solution_instance.candy([1,2,87,87,87,2,1]))
