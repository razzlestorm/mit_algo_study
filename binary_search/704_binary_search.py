class Solution:
    def search(self, nums, target: int) -> int:
        """Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1."""
        counter = 0
        while len(nums) > 0:
            mid = len(nums)//2
            if nums[mid] == target:
                return mid+counter
            if len(nums) <= 1:
                return -1
            if nums[mid] < target:
                nums = nums[mid:]
                counter += mid
            else:
                nums = nums[:mid]
        return -1
