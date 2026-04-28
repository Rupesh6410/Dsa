class Solution:
    def return_nicely(self, i: int, j: int) -> List[int]:
        return [i+1, j+1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            my_sum = numbers[i] + numbers[j]
            if my_sum == target:
                return self.return_nicely(i, j)
            if my_sum < target:
                i += 1
                continue
            j -= 1
        return []
