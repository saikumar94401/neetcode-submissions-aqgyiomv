class Solution {
    public int change(int amount, int[] coins) {
        int dp[] = new int[amount+1];
        
        for(int i=0;i<dp.length;i++)
        {
            dp[i]=0;
        }
        dp[0]=1;


        for(int coin=0; coin<coins.length;  coin++)
        {
            for(int am=1;am<dp.length;am++)
            {  
               


                if(am>=coins[coin] && dp[am-coins[coin]]!=0)
                    dp[am]+=dp[am-coins[coin]];
                    
            }
        }

        
        return dp[amount];

    }
}
