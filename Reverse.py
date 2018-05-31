"""
Problem:
        Given a 32-bit signed integer, reverse digits of an integer.
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r=(x>0)-(x<0)
        s = int(str(r*x)[::-1]) 
        return s*r*(s<2**31)
		
		
		

class Solution:
    def reverse(self, x):
	    """
	    :type x: int
        :rtype: int
        """
		r = 0
		if x <0:
		   flag = True
		   a = -x
		   if x < -2**31:
		      return 0
		else:
		   flag = False
		   a = x
		   if x > 2**31：
		      return 0
		while 1:
		    r += a%10
			a = a//10
			if not a:
			   break
			r = r*10
		ret = r*(-1) if flag else r
		return ret if r<2**31 else 0