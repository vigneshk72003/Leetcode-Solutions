class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i,j;
        int temp;
        int n=nums.size();
        i=0;
        for(j=0;j<n;j++)
        {        
            if(nums[j]!=0)
            {
                    temp =nums[j];
                    nums[j]=nums[i];
                    nums[i]=temp;
                    i++;
            }                
        }
        for(int k=0;k<n;k++)
        {
            cout<<nums[k]<<",";
        }   
    }
};