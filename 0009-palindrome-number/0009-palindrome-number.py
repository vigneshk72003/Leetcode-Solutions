class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        count=0
        for i in range(0,len(y)/2,1):
            if(y[i]==(y[len(y)-i-1])):
                continue
            else:
                count=count+1
        if(count!=0):
            return False
        else:
            return True

          

        