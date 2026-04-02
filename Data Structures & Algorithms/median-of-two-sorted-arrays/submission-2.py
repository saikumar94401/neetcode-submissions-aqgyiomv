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
                l1 = mid-1
                r1=mid
                l2 = median-mid-1
                r2=median-mid
                if r2<n2 and l1>=0 and nums1[l1] > nums2[r2]:
                    e=mid-1
                elif r1<n1 and l2>=0 and nums2[l2] > nums1[r1] :
                    s=mid+1
                else:
                    rmax=0
                    lmax=0
                    if r1==n1:
                        rmax=nums2[r2]
                    elif r2==n2:
                        rmax=nums1[r1]
                    else:
                        rmax=min(nums1[r1],nums2[r2])
                    if length%2==0:
                        if l1<0:
                            lmax=nums2[l2]
                        elif l2<0:
                            lmax=nums1[l1]
                        else:   
                            lmax=max(nums1[l1],nums2[l2])
                        return (lmax+rmax)/2
                    else:
                        return float(rmax)
        n1=len(nums1)
        n2=len(nums2)
        if n1<=n2:
            return binarySearch(nums1,nums2,n1,n2)
        else:
            return binarySearch(nums2,nums1,n2,n1)
            

