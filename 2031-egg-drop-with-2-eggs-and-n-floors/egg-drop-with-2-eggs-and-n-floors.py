class Solution(object):
    def twoEggDrop(self, n):
        i=1
        while(i*(i+1)) //2 < n:
            i+=1
        return i        