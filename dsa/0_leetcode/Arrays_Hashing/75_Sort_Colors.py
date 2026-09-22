class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            k = i
            j = i - 1
            while j >= 0 and nums[j] > nums[k]:
                nums[k], nums[j] = nums[j], nums[k]
                j = j - 1
                k = k - 1


sol = Solution()
sol.sortColors(nums=[2, 0, 2, 1, 1, 0])
