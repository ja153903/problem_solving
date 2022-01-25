from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # find point of inflection
        # if there is more than 1, then we know that this is incorrect
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                j, k = i - 1, i + 1

                while j >= 0 or k < len(arr):
                    if j >= 0:
                        if j > 0 and arr[j] <= arr[j - 1]:
                            return False
                        j -= 1

                    if k < len(arr):
                        if k < len(arr) - 1 and arr[k] <= arr[k + 1]:
                            return False
                        k += 1

                return True

        return False
