class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        l=len(n)
        c=0
        for i in range(l//2):
                if n[i]==n[l-1-i]:
                    c+=1
        if c==l//2:
                       return True
        else:
                       return False   