class Solution {
    int coinChange(int i,int amount,int coins[],int dp[][])
    {
        if( i==coins.length )
            return 0;
         if(amount==0)
            return 1;

        if( amount<0 || amount<coins[i])
            return 0;
       
        if(dp[i][amount]!=-1)
            return dp[i][amount];

        return dp[i][amount]=coinChange(i,amount-coins[i],coins,dp)+coinChange(i+1,amount,coins,dp);

    }
    public int change(int amount, int[] coins) {
    int dp[][] = new int[coins.length][amount+1];
    Arrays.sort(coins);
    for(int i=0;i<coins.length;i++)
        for(int j=0;j<amount+1;j++)
            dp[i][j]=-1;
    return coinChange(0,amount,coins,dp);

    }
}