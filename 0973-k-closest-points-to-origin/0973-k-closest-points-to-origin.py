class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        x=[]
        z=[]
        for i in range(len(points)):
            s=points[i][0]**2+points[i][1]**2
            x.append([points[i],s])
        y=sorted(x,key=lambda a:a[1])
        for i in range(k):
            z.append(y[i][0])
        return z
        