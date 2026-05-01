class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        n = len(arr)
        ans = 0

        for i in range(n - 2):
            l = i + 1
            r = n - 1

            while l < r:
                curr_sum = arr[i] + arr[l] + arr[r]

                if curr_sum < sum:
                    ans += (r - l)   
                    l += 1
                else:
                    r -= 1

        return ans