class Solution(object):
    def maximumWealth(self, accounts):
        richest=0
        for i in range(len(accounts)):
            total=0
            for j in range(len(accounts[i])):
                total = total + accounts[i][j]
                if total > richest :
                 richest= total
        return richest
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        