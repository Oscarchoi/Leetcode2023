# 852. Peak Index in a Mountain Array - Medium

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        head = 0
        tail = len(arr) - 1

        while True:
            n = int((tail + head) / 2)

            front = (arr[n] > arr[n-1])
            rear = (arr[n+1] < arr[n])

            if front and rear:
                return n
            elif front and not rear:
                head = n
            elif not front and rear:
                tail = n
            else:
                break

        return 0
