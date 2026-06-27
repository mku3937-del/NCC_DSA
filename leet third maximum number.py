class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m = set(nums)
        s = list(m)
        s.sort()
        if len(s) >= 3:
            return s[len(s) - 3]
        else:
            return max(s)