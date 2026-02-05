class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] == 0:
                result[i] = 0
            else:
                result[i] = nums[(i + nums[i]) % n]

        return result
