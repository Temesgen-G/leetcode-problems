class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        counter=0
        for i in range(1,len(nums)):
            diff=nums[i-1]-nums[i]
            if nums[i]<nums[i-1]:
                counter+=diff+1
                nums[i]+=diff+1
            
            elif nums[i]==nums[i-1]: 
                counter+=1
                nums[i]+=1
        return counter  
        