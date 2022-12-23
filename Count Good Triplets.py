class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count=0
        if len(arr)<3:
            return 0
    
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                for k in range(2,len(arr)):
                    if i>=0 and j>i and k>j and len(arr)>k:
                        if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                            count+=1
                        
        return count
