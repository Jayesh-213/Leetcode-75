 class Solution:
    def reverseWords(self, s: str) -> str:
       j= s.split()
       j.reverse()
       return " ".join(j)
