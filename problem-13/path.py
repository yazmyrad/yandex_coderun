"""
Docstring for problem_13

problem №13 - Путь в графе
link to the problem - https://coderun.yandex.ru/problem/the-path-in-the-graph
difficulty - medium
tag - bfs

"""


"""
Input: 
    First line - integer N  ( 1 ≤ N ≤ 100 ).
    In the next N lines there is adjacency matrix of graph row by row

Output:
    if path exists in first line output the length L and in the next line th path itself.
    if path doesn't exist output -1
"""

import sys
from collections import deque

def main():
    n = int(input())
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    start, end = map(int, input().split())
    if start == end:
        print(0)
        return
    que = deque()
    que.append(start-1)
    visited = [False]*n
    visited[start-1] = True
    
    answer = []
    parents = [-1]*n
    path_exists = False
    while que:
        source = que.popleft()
        if source == end-1:
            path_exists = True
            break
        for neigh in range(n):
            if graph[source][neigh] == 1 and visited[neigh] != True:
                que.append(neigh)
                visited[neigh] = True
                parents[neigh] = source

    if not path_exists:
        print(-1)
        return
    else:
        node = end-1
        while node != -1:
            answer.append(node+1)
            node = parents[node]

        print(len(answer)-1)
        print(*answer[::-1])



if __name__ == '__main__':
    main()