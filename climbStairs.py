"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        cum = [0]*(n+1)
        cum[1], cum[2] = 1, 2
        for i in range(3, n+1):
            cum[i] = cum[i-1] + cum[i-2]
        return cum[n]                                                                                                                            