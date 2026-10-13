class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for j in adj[i]:
                dfs(j)

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count