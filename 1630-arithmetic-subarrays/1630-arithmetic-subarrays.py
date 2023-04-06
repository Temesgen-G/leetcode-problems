class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        x=[]
        
        for i in range(len(l)):
            sub=nums[l[i]:r[i]+1]
            sub.sort()
            diff=sub[1]-sub[0]
            y=True
            for j in range(2,len(sub)):
                if diff!=sub[j]-sub[j-1]:
                    y=False
                    break
            x.append(y)
        return x 
       
        