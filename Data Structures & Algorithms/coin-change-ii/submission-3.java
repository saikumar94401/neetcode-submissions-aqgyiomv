class Solution {
    public int change(int amount, int[] coins) {
        int dp[][] = new int[coins.length+1][amount+1];
        if(amount==0 && coins.length!=0)
            return 1;
        for(int coin=0;coin<dp.length;coin++)
        {
            for(int am=0;am<dp[0].length;am++)
            {   // fill the first row and column with zeros
                if(am==0 || coin==0){
                    dp[coin][am]=0;
                    continue;
                }
                
                // carry forward previous rows solution
                dp[coin][am]=dp[coin-1][am];
                
                int sub_amount=coins[coin-1];

                if(am<sub_amount)
                    continue;
                
                
                if(am-sub_amount==0)
                    dp[coin][am]+=1;
                else if(dp[coin][am-sub_amount]!=0)
                    dp[coin][am]+=dp[coin][am-sub_amount];
            }
        }

        
        return dp[coins.length][amount];

    }
}
