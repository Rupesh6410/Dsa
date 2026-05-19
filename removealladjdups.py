class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=[]
        for ch in s:
            if a and a[-1]==ch:
                a.pop()
            else:
                a.append(ch)
        return "".join(a)
        
            