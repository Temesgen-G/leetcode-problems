class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
        j=int(len(piles)-1)
    
        n=int(len(piles)/3)
        
        
        z=piles[ :(j-(n-1))]
        i=1
        sum=0
        while i<len(z):
            
            sum+=z[i]
            i+=2
        
        
        
        
        
        
        
        
            
        return sum
        
            
            
                
        
        