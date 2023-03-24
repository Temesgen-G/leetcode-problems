class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        i=0
        j=len(nums)-1
        z=0
        while i<j:
            z=max((nums[i]+nums[j]),z)
            i+=1
            j-=1
        
        
        return z