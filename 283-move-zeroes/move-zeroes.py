class Solution(object):
    def moveZeroes(self, nums):
        key=0
        for i in range(len(nums)):
            if nums[i] !=  0:
                nums[key],nums[i]=nums[i],nums[key]
                key+=1
        return nums
     
        