class Solution {
    public int maxSubArray(int[] nums) {
        int temp=0;
        int result=nums[0];
        for(int i=0;i<nums.length;i++)
        {
            temp+=nums[i];
            result=Math.max(temp,result);
            if(temp<0)
            {
                temp=0;
            }
        }
        return result;
    }
}