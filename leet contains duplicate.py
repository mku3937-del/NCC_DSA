class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test = set(nums)
        if len(test) != len(nums):
            return True
        else:
            return False