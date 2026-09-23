class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0

        # Sort the array to easily pick min/max transitions
        arr.sort()

        # Initial difference without modifications (or applying same operation to all)
        ans = arr[-1] - arr[0]

        smallest = arr[0] + k
        largest = arr[-1] - k

        for i in range(n - 1):
            min_height = min(smallest, arr[i + 1] - k)
            max_height = max(largest, arr[i] + k)

            # Skip invalid heights (height cannot be negative)
            if min_height < 0:
                continue

            ans = min(ans, max_height - min_height)

        return ans