class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1
        v = self.myPow(x, n // 2)
        if n % 2 == 0:
            return v * v

        else:
            return v * v * x