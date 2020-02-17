from typing import *

# needs to be direct acyclic graph
# topological sort implemented using depth first search

def topological_sort(asg: List[List[int]])->List[int]:
    seen = [False] * len(asg)

    def dfs(start: int, stack: List[int]):
        nonlocal seen
        for dest, exists in enumerate(asg[start]):
            if exists and not seen[dest]:
                dfs(dest, stack)
                stack.append(dest)
                seen[dest] = True

    topographically_sorted = []
    for i in range(len(asg)):
        if not seen[i]:
            seen[i] = True
            stack = [i]
            dfs(i, stack)
            while stack:
                topographically_sorted.append(stack.pop())

    return topographically_sorted



if __name__ == '__main__':
    adj_matrix = [[0] * 6 for _ in range(6)]

    adj_matrix[5][2] = 1
    adj_matrix[5][0] = 1
    adj_matrix[2][3] = 1
    adj_matrix[3][1] = 1
    adj_matrix[4][0] = 1
    adj_matrix[4][1] = 1
    print(topological_sort(adj_matrix))