class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        idx = 0
        ans = []
        diary = []
        sums = 0

        def comb(candidates, n, idx, ans, diary, sums, target):
            if sums == target:
                ans.append(diary.copy())
                return

            if idx == n or sums > target:
                return

            
            comb(candidates, n, idx + 1, ans, diary, sums, target)

            
            diary.append(candidates[idx])
            sums += candidates[idx]

            comb(candidates, n, idx, ans, diary, sums, target)

            diary.pop()
            sums -= candidates[idx]

        comb(candidates, n, idx, ans, diary, sums, target)

        return ans
