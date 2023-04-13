class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=0
        n=int(len(arr)/2)
        b=[]
        x=Counter(arr)
        w=sorted(x.values(),reverse=True )

        for i in range(len(w)):
            if c+w[i]>=n:
                i=i+1
                break
            c+=w[i]

        return i

      
        