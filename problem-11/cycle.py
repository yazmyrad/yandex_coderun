"""
Docstring for problem_10

problem №11 - Поиск цикла
link to the problem - https://coderun.yandex.ru/problem/cycle-search
difficulty - medium
tag - dfs

"""


"""
Input: 
    First line - integer N  ( 1 ≤ N ≤ 500 ).
    In the next N lines there is adjacency matrix of graph row by row

Output:
    String 'NO',
    String 'YES' with number of nodes in cycle and the nodes itself
"""
import sys


def main():
    n = int(input())
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    state = [0]*n
    cycle = [False]
    cycle_nodes = []
    parents = [-1]*n
    def dfs(u, parent): 
        state[u] = 1
        parents[u] = parent
        for v in range(n):
            if graph[u][v] == 1:
                if parent == v:
                    continue
                
                if state[v] == 0:
                    dfs(v, u)
                    if cycle[0]:
                        return
                elif state[v] == 1:
                    cycle_nodes.clear()
                    cycle_nodes.append(v+1)
                    
                    curr = u 
                    while curr != v:
                        cycle_nodes.append(curr+1)
                        curr = parents[curr]
                    cycle[0] = True
                    return
        state[u] = 2
    
    for i in range(n):
        if not cycle[0] and state[i] == 0:
            dfs(i, -1)
    
    if cycle[0]:
        print('YES')
        print(len(cycle_nodes))
        print(*cycle_nodes[::-1])
    else:
        print('NO')


if __name__ == '__main__':
    main()