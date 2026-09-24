class Solution:
    def reverseDegree(self, s: str):
        j,sum=len(s),0
        for i in range(1,j+1):
            sum+=i*(26-(ord(s[i-1])-97))
        return sum