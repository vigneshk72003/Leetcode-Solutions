class Solution(object):
    def hammingDistance(self, x, y):
       x_bin=str(bin(x)[2:])
       y_bin=str(bin(y)[2:])
       count=0
       if(len(x_bin)>len(y_bin)):
        y_bin="0"*(len(x_bin)-len(y_bin))+y_bin
       else:
        x_bin="0"*(len(y_bin)-len(x_bin))+x_bin
       for i in range(len(x_bin)-1,-1,-1):
        if (x_bin[i]!=y_bin[i]):
            count=count+1
       return count