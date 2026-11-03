class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(arr, n):
            t = 0
            for i in arr:
                t += math.ceil(i / n)
            return t

        left, right = 1, max(piles)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if totalTime(piles, mid) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans