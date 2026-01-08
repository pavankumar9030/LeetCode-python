class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = nums1[0] * nums2[0]
        for i in range(1, n):
            dp[i][0] = max(nums1[i] * nums2[0], dp[i-1][0])
        for j in range(1, m):
            dp[0][j] = max(nums1[0] * nums2[j], dp[0][j-1])
        for i in range(1, n):
            for j in range(1, m):
                prod = nums1[i] * nums2[j]
                dp[i][j] = max(prod + max(0, dp[i-1][j-1]),
                               dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
