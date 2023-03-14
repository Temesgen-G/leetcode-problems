class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x=range(1,n+1)
        y=[]
        for i in x:
            if i%3==0 and i%5==0:
                y.append("FizzBuzz")
            elif i%3==0:
                y.append("Fizz")
            elif i%5==0:
                y.append("Buzz")
            else:
                y.append(str(i))
        return y
    

        