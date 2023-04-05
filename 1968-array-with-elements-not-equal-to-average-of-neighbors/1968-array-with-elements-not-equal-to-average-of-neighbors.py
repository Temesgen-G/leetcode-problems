class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        
        z=[nums[0]]
        i=1
        
        
    
        while len(z)<=len(nums):
            z.append(nums[len(nums)-i])
            z.append(nums[i])
            i+=1
        w=z[:len(nums)]
            
             
        
        return w
        
        