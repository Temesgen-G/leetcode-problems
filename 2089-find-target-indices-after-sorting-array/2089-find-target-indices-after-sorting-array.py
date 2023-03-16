class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        y=[]
        for i in range(len(nums)):
            
            
            if nums[i]==target:
                y.append(i)
        return y
        