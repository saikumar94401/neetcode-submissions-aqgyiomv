class Solution {
    
    int commonSubsequence(int i,int j,String text1,String text2,int dp[][])
    {
        if(i==text1.length() || j==text2.length()) return 0;
        if(dp[i][j]!=-1)
            return dp[i][j];
        int temp1=0;
        if(text1.charAt(i)==text2.charAt(j))
        {
            temp1=Math.max(temp1,1+commonSubsequence(i+1,j+1,text1,text2,dp));
        }
        else{
        int temp2=Math.max(commonSubsequence(i+1,j,text1,text2,dp),commonSubsequence(i,j+1,text1,text2,dp));
        temp1=Math.max(temp1,temp2);
        }
        return dp[i][j]=temp1;
    }
    public int longestCommonSubsequence(String text1, String text2) {
        int l1=text1.length();
        int l2=text2.length();
        int dp[][]=new int[l1][l2];
        for(int i=0;i<l1;i++)
            for(int j=0;j<l2;j++)
                dp[i][j]=-1;
        return commonSubsequence(0,0,text1,text2,dp);



        
    }
}