class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=0
        n=int(len(arr)/2)
        b=[]
        x=Counter(arr)
        y=dict(sorted(x.items(),key=lambda a:a[1],reverse=True ))
        z=list(y.keys())
        w=list(y.values())
        for i in range(len(w)):
            if c+w[i]>=n:
                d=z[:i+1]
                break
            c+=w[i]
        s=len(d)
        return s
        
      
        