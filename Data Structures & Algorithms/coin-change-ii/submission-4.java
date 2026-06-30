class Solution {
    public int change(int amount, int[] coins) {
        int dp[][] = new int[coins.length+1][amount+1];
        
        for(int coin=0;coin<dp.length;coin++)
        {
            for(int am=0;am<dp[0].length;am++)
            {   // fill the first row  with zeros
                if(coin==0){
                    dp[0][am]=0;
                    continue;
                }
                // fill the first row and column with zeros
                if(am==0)
                {
                    dp[coin][0]=1;
                    continue;
                }
                
                
                // carry forward previous rows solution
                dp[coin][am]=dp[coin-1][am];
                
                int sub_amount=coins[coin-1];

                if(am>=sub_amount && dp[coin][am-sub_amount]!=0)
                    dp[coin][am]+=dp[coin][am-sub_amount];
                    
            }
        }

        
        return dp[coins.length][amount];

    }
}
