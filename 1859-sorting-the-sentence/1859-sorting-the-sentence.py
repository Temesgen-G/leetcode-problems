class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        z = [int(''.join(filter(str.isdigit, y))) for y in x]
        x = sorted(x, key=lambda a: z[x.index(a)])
        new_list=[str(''.join(filter(str.isalpha, item))) for item in x]
        my_list= ' '.join(new_list)
        return my_list