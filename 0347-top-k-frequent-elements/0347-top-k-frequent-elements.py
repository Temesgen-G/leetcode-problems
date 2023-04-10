class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        z=defaultdict(bool)
        for i in range(len(nums)):
            if not z[nums[i]]:
                z[nums[i]]=[i]
            else:
                z[nums[i]].append(i)
        x=dict(sorted(z.items(),key=lambda a:len(a[1])))
        y=list(x.keys())
        y.reverse()
        w=y[:k]
    
      
        return w
                
            
        