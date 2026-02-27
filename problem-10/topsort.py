"""
Docstring for problem_10

problem №10 - Топологическая сортировка
link to the problem - https://coderun.yandex.ru/problem/topological-sorting
difficulty - medium
tag - topsort

"""


"""
Input: 
    First line - integers N, M  ( 1 ≤ N,M ≤ 100 000 ).
    In the next M lines there are edges of graph

Output:
    array of nodes or -1
"""

def main():
    n, m = map(int, input().split())
    graph = {i:[]for i in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    state = [0]*n 
    stack = []
    hasCycle = [False]
    def dfs(node):
        if hasCycle[0]:
            return 
        state[node-1] = 1
        for neigh in graph[node]:
            if state[neigh-1] == 0:
                dfs(neigh)
            elif state[neigh-1] == 1:
                hasCycle[0] = True
                return
            
        stack.append(node)
        state[node-1] = 2
        return
        
    for i in range(1, n+1):
        if state[i-1] == 0 and not hasCycle[0]:
            dfs(i)

    print(*stack[::-1]) if not hasCycle[0] else print(-1)

if __name__=="__main__":
    main()