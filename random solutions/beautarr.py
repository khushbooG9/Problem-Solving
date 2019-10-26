class Solution(object):
    
    def countArrangement(self, N):
        self.count = 0
        visited = [False]*(N+1)
        
        def calc(N, pos, visited):
        
            if pos>N:
                self.count +=1
            for i in range(1,N+1):
                if visited[i]==False and (pos%i==0 or i%pos==0):
                    visited[i]=True
                    calc(N,pos+1,visited)
                    visited[i] = False
        
        calc(N,1,visited)
        return self.count
        