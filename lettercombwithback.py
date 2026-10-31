class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def solve(i=0, temp=""):

            if i == len(digits):
                ans.append(temp)
                return

            letters = phone[digits[i]]

            for ch in letters:
                temp += ch
                solve(i+1, temp)
                temp = temp[:-1]

        solve()

        return ans
            
