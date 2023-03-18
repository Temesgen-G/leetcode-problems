class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        x=[int(j) for j in nums]
        x.sort()
        x.reverse()
        for i in range(len(x)):
            if i==k:
                str(x[k-1])
        return str(x[k-1]) 
        