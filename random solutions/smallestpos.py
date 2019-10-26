"""
class Solution(object):
    def firstMissingPositive(self, nums):
        
        
        if not nums:
            return 1
        if len(nums)==1:
            return 2 if nums[0]==1 else 1
        m = max(nums)
        l = [0]*m
        for n in nums:
            if n>0:
                if l[n-1]!=1:
                    l[n-1]=1
        for j in range(len(l)):
            if l[j]==0:
                return j+1
        return len(l)+1
"""
class Solution(object):
    
    def sep(self, a, size):
        j=0
        for i in range(size):
            if a[i]<=0:
                t = a[i]
                a[i]=a[j]
                a[j]=t
                j+=1
        return j
    
    def fmphelper(self, a, size):
        for i in range(size):
            if (abs(a[i])-1<size)  and a[abs(a[i])-1]>0 :
                a[abs(a[i])-1] = -a[abs(a[i])-1]
        
        for j in range(size):
            if a[j]>0:
                return j+1
        return size+1
    
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        shift = self.sep(nums, len(nums))
        return self.fmphelper(nums[shift:], len(nums)-shift)
        