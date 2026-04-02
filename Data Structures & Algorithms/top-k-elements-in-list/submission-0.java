class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> hmap = new HashMap<>();
        for(int n:nums)
        {
            if(hmap.containsKey(n))
            {
                hmap.put(n,hmap.get(n)+1);
            }
            else{
                hmap.put(n,1);
            }
        }
         for(Map.Entry<Integer,Integer> entry: hmap.entrySet())
        {
            System.out.println(entry.getKey()+":"+entry.getValue());
        }

        List<Integer>[] freq = new List[nums.length+1];
        for(int i=0;i<freq.length;i++)
        {
            freq[i]=new ArrayList<>();
        }
       
        for (Map.Entry<Integer, Integer> entry : hmap.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        // int res[]= new int[k];
        // int index=0;
        // for(int i=freq.length-1;i>0 && index< k;i--)
        // {
          
        //     for(int n:freq[i])
        //     {
        //         System.out.println(n);
        //         res[index++]=n;
        //         if(index == k)
        //             break;
        //     }
           
        // }
       
        
      
          int[] res = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (int n : freq[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return res;

        
        

        

        
    }  
}