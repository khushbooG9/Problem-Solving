class Solution(object):
    
    def comp(self,a,b):
        for i in range(256):
            if a[i]!=b[i]:
                return False
        return True
    
    def findAnagrams(self, s, p):
        res = []
        countp = [0]*256
        countw = [0]*256
        if len(s)<len(p):
            return res
        for i in range(len(p)):
            countp[ord(p[i])]+=1
            countw[ord(s[i])]+=1
        for k in range(len(p), len(s)):
            if self.comp(countp, countw):
                res.append(k-len(p))
            countw[ord(s[k])]+=1
            countw[ord(s[k-len(p)])]-=1
        if self.comp(countp, countw):
            res.append(len(s)-len(p))
        return res