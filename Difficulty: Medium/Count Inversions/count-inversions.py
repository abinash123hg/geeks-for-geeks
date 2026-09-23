class Solution:
    def inversionCount(self, arr):
        def merge_and_count(arr, temp, left, mid, right):
            i = left    # Starting index for left subarray
            j = mid + 1 # Starting index for right subarray
            k = left    # Starting index to be merged
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            for idx in range(left, right + 1):
                arr[idx] = temp[idx]

            return inv_count

        def merge_sort_and_count(arr, temp, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                inv_count += merge_sort_and_count(arr, temp, left, mid)
                inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
                inv_count += merge_and_count(arr, temp, left, mid, right)

            return inv_count

        n = len(arr)
        temp = [0] * n
        return merge_sort_and_count(arr, temp, 0, n - 1)