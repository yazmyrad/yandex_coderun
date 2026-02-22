"""
Docstring for problem_9

problem №9 - Списывание
link to the problem - https://coderun.yandex.ru/problem/cheating
difficulty - medium
tag - DFS

"""


"""
Input: 
    First line - integers N, M  ( 1 ≤ N ≤ 10^2, 0 ≤ M ≤ N ( N − 1 ) / 2 ).
    In the next M lines there are two integers up to N

Output:
    String, YES/NO
"""

def main():
    n, m = map(int, input().split())
    graph = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v) 
        graph[v].append(u)

    colors = [-1]*n
    answer = True
    for i in range(1, n+1):
        if colors[i-1] != -1:
            continue
        stack = [i]
        colors[i-1] = 0
        while stack:
            node = stack.pop()
            for neigh in graph[node]:
                if colors[neigh-1] == -1:
                    stack.append(neigh)
                    colors[neigh-1] = 1 - colors[node-1]

                elif colors[neigh-1] == colors[node-1]:
                    answer = False
                    break

    print('YES' if answer else 'NO')

if __name__ == "__main__":
    main()