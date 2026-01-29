class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        N = 26 
        
        dist = [[INF] * N for _ in range(N)]
        
        for i in range(N):
            dist[i][i] = 0
        
   
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
     
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        
        total = 0
        for s, t in zip(source, target):
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]
        
        return total

        