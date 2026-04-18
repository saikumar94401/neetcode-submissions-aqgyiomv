class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        most_freq=max(freq.values())
        max_count=0
        for val in freq.values():
            if val==most_freq:
                max_count+=1
        
        min_req=(most_freq-1)*(n+1)

        return max(len(tasks),min_req+max_count)
