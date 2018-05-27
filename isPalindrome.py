"""Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward."""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        if x<0:
           return False
        else:
            a = str(x)
            l = len(a)
            count = 0
            if l%2 == 0:
              for i in range(int(l/2)):
                 if a[i]== a[-i-1]:
                   count += 1
              if count == int(l/2):
                 return True
              else:
                 return False

            else:
               for j in range(int(l/2)):
                   if a[j]==a[-j-1]:
                      count +=1
               if count == int(l/2):
                 return True 
               else:
                 return False