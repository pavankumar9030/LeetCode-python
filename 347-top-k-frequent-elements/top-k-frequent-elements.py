class Solution(object):
    def topKFrequent(self, nums, k):
        frequency={}
        for num in nums:
            if num not in frequency:
                frequency[num]=1
            else:
                frequency[num] += 1
        sorted_items=sorted(frequency.items(),key=lambda x: x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(sorted_items[i][0])
        return result