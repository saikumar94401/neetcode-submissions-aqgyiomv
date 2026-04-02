class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def binarySearch(nums1,nums2,n1,n2) :
            length=n1+n2
            median=(length)//2
            s=0
            e=n1
            while s<=e:
                mid=s+(e-s)//2
                print(mid)
                l1 = nums1[mid-1] if mid>0 else float("-inf")
                r1=nums1[mid]     if mid<n1 else float("inf")
                l2 = nums2[median-mid-1] if (median-mid)>0 else float("-inf")
                r2=nums2[median-mid] if median-mid<n2 else float("inf")
                if l1 > r2:
                    e=mid-1
                elif  l2 > r1 :
                    s=mid+1
                else:
                    rmax=min(r1,r2)
                    if length%2==0:    
                        lmax=max(l1,l2)
                        return (lmax+rmax)/2
                    else:
                        return float(rmax)
        n1=len(nums1)
        n2=len(nums2)
        if n1<=n2:
            return binarySearch(nums1,nums2,n1,n2)
        else:
            return binarySearch(nums2,nums1,n2,n1)
            

