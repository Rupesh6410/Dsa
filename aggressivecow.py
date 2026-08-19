class Solution:
    def aggressiveCows(self, arr, k):
        
        arr.sort()

        low = 1
        high = arr[-1] - arr[0]

        def isTrue(x, k):
            cows = 1
            last = arr[0]

            for i in range(1, len(arr)):
                if arr[i] - last >= x:
                    cows += 1
                    last = arr[i]

                    if cows == k:
                        return True

            return False

        while low <= high:
            mid = (low + high) // 2

            if isTrue(mid, k):
                low = mid + 1
            else:
                high = mid - 1

        return high
        
