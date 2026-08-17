class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        pre_map={i:[] for i in range(n)}
        for crs,pre in prerequisites:
            pre_map[crs].append(pre)
        visited=[0]*(n)
        def dfs(crs):
            if visited[crs]==1:
                return False
            if visited[crs]==2:
                return True
            visited[crs]=1
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visited[crs]=2
            return True
        for crs in range(n):
            if not dfs(crs):
                return False
        return True