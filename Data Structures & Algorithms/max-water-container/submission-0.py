class Solution:
    def maxArea(self, hts: List[int]) -> int:
        left, right = 0, len(hts) - 1
        max_area = 0

        while right > left:
            width = right - left
            height = min(hts[left], hts[right])

            area = width * height
            max_area = max(max_area, area)

            if hts[left] < hts[right]:
                left += 1
            else:
                right -= 1

        return max_area