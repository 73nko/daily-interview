###
# 17-11-2020
# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]
###

class Solution:
    def getRange(self, arr, target):
        low = 0
        high = len(arr)-1
        first = self.binarySearch(arr, low, high, target, True)
        last = self.binarySearch(arr, low, high, target, False)
        return [first, last]

    def binarySearch(self, arr, low, high, target, findLowest):
        if(high >= low):
            mid = int(low + (high - low) / 2)
            if findLowest:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    return self.binarySearch(arr, mid + 1, high, target, findLowest)
                else:
                    return self.binarySearch(arr, low, mid - 1, target, findLowest)
            else:
                if (mid == len(arr)-1 or x < arr[mid + 1]) and arr[mid] == x:
                    return mid
                elif target < arr[mid]:
                    return self.binarySearch(arr, low, mid - 1, target, findLowest)
                else:
                    return self.binarySearch(arr, mid + 1, high, target, findLowest)
        return -1


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
