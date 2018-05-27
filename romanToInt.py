"""Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = str(s)
        count = 0
        for i in range(len(s)):

            if s[i] == "I":
               count +=  1
            elif s[i] == "V":
               count += 5
            elif s[i] == "X":
               count += 10
            elif s[i] == "L":
               count += 50
            elif s[i] == "C":
               count += 100
            elif s[i] == "D":
               count += 500
            elif s[i] =="M":
               count += 1000
        for j in range(len(s)-1):
             if (s[j]== "I") and (s[j+1] !="I"):
                count -= 2
             elif (s[j]=="X") and (s[j+1] != "I" and s[j+1]!= "V" and s[j+1]!= "X"):
                count -=20
             elif (s[j]=="C") and (s[j+1] =="D" or s[j+1]=="M"):
                count -=200
        return count 