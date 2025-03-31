class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
            
        def merge(lH,rH):
            r=l=0
            mergedarr=[]
            while l<len(lH) and r<len(rH):
                if lH[l]<rH[r]:
                    mergedarr.append(lH[l])
                    l+=1
                else:
                    mergedarr.append(rH[r])
                    r+=1
            mergedarr.extend(lH[l:])
            mergedarr.extend(rH[r:])
            return mergedarr
        
        def mergeSort(left,right,arr):
            if left==right:
                return[arr[left]]
            mid=left+(right-left)//2
            leftHalf=mergeSort(left,mid,arr)
            rightHalf=mergeSort(mid+1,right,arr)
            return merge(leftHalf,rightHalf)
        return mergeSort(0,len(nums)-1,nums)
                