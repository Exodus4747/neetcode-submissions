class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lst = []
        for i in range(len(arr)-1):  
            maxe = arr[i+1]           
            for j in range(i+1,len(arr)):

                if   arr[j] > maxe :    
                    maxe = arr[j]  
            lst.append(maxe)
        lst.append(-1)
        return lst