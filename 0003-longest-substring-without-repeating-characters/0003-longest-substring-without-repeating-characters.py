class Solution(object):
    def lengthOfLongestSubstring(self, s):
       i=0
       j=0
       s=str(s)
       maximum=0
       while(i<len(s)):
            list=[]
            for j in range(i,len(s),1):
                if s[j] not in list:
                    list.append(s[j])
                else:
                    break
            i=i+1
            maximum=max(maximum,len(list))
            # if(max<len(list)):
            #     max=len(list)
       return maximum