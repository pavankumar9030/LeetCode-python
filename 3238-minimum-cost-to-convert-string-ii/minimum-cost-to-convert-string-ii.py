class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        MOD = (1 << 61) - 1
        BASE = 911382323
        n = len(source)

        def h(s):
            v = 0
            for c in s:
                v = (v * BASE + ord(c)) % MOD
            return v

        by_len = {}
        for o, c, w in zip(original, changed, cost):
            L = len(o)
            ho, hc = h(o), h(c)
            if L not in by_len:
                by_len[L] = {}
            by_len[L].setdefault(ho, {})
            by_len[L].setdefault(hc, {})
            by_len[L][ho][hc] = min(by_len[L][ho].get(hc, INF), w)

        dist = {}
        for L, g in by_len.items():
            nodes = list(g.keys())
            idx = {x: i for i, x in enumerate(nodes)}
            m = len(nodes)
            d = [[INF] * m for _ in range(m)]
            for i in range(m):
                d[i][i] = 0
            for u in g:
                for v in g[u]:
                    d[idx[u]][idx[v]] = g[u][v]
            for k in range(m):
                for i in range(m):
                    for j in range(m):
                        if d[i][k] + d[k][j] < d[i][j]:
                            d[i][j] = d[i][k] + d[k][j]
            dist[L] = (nodes, idx, d)

        def build(s):
            H = [0] * (n + 1)
            P = [1] * (n + 1)
            for i in range(n):
                H[i + 1] = (H[i] * BASE + ord(s[i])) % MOD
                P[i + 1] = (P[i] * BASE) % MOD
            return H, P

        def sub(H, P, l, r):
            return (H[r] - H[l] * P[r - l]) % MOD

        hs, ps = build(source)
        ht, pt = build(target)

        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            for L in dist:
                if i + L > n:
                    continue
                a = sub(hs, ps, i, i + L)
                b = sub(ht, pt, i, i + L)
                nodes, idx, d = dist[L]
                if a in idx and b in idx:
                    dp[i] = min(dp[i], d[idx[a]][idx[b]] + dp[i + L])

        return -1 if dp[0] == INF else dp[0]
