class Solution:
    def intersection(self, nums):

        count = {}

        for arr in nums:

            for num in arr:

                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1

        result = []

        for key in count:

            if count[key] == len(nums):
                result.append(key)

        result.sort()

        return result