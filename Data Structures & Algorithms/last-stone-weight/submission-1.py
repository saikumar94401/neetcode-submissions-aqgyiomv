class Solution:
    def parent(self,index) :
        return (index-1)//2

    def left(self,index):
        return index*2+1
    
    def right(self,index):
        return index*2+2
    
    def swap(self,first,second,max_heap) :
        temp= max_heap[first]
        max_heap[first]=max_heap[second]
        max_heap[second]=temp

    def upHeap(self,max_heap,index) :
        if index <0:
            return 

        parent=self.parent(index)
        if parent>=0:
            if max_heap[parent]<max_heap[index] :
                self.swap(parent,index,max_heap) 
            else:
                return
        self.upHeap(max_heap,parent)

    def downHeap(self,index,max_heap) :
        left=self.left(index)
        right=self.right(index)
        maxi=index
        if left < len(max_heap) and max_heap[left] > max_heap[maxi] :
            maxi=left
        if right <len(max_heap) and max_heap[right] > max_heap[maxi]:
            maxi=right
        if maxi!=index :
            self.swap(index,maxi,max_heap)
        else:
            return
        
        self.downHeap(maxi,max_heap)
    def getMax(self,max_heap) :
        maximum=max_heap[0]
        print(maximum)
        last=max_heap.pop()
        if len(max_heap) >0 :
            max_heap[0]=last
            self.downHeap(0,max_heap)
        return maximum
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[]
        for stone in stones:
            max_heap.append(stone)
            self.upHeap(max_heap,len(max_heap)-1)
        print(max_heap)

        while len(max_heap)>1 :
            first=self.getMax(max_heap)
            second=self.getMax(max_heap)

            if first!=second:
                diff=first-second
                max_heap.append(diff)
                self.upHeap(max_heap,len(max_heap)-1)
            
        if len(max_heap)==0:
            return 0
        return max_heap[0]


        