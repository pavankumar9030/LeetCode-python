class Solution(object):
    def intersection(self, nums):
        result=[]
        for i in nums[0]:
            found=True
            for j in range(1,len(nums)):
                if i not in nums[j]:
                    found=False
                    break
            if found==True:
                result.append(i)
        return sorted(result)
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        