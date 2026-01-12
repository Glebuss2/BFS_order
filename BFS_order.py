def bfs_order(n: int, adj: list[list[int]], start: int) -> list[int]:
    if n == 0:
        return []
    if not (0 <= start < n):
        raise ValueError("стартовая вершина вне диапазона [0, n-1]")

    visited = [False] * n
    q = [start]
    head = 0
    visited[start] = True
    order = []

    while head < len(q):
        v = q[head]
        head += 1
        order.append(v)

        for to in adj[v]:
            if not visited[to]:
                visited[to] = True
                q.append(to)

    return order


def main():
    with open("input.txt", "r") as f:
        tokens = f.read().strip().split()

    if not tokens:
        with open("output.txt", "w") as out:
            out.write("")
        return

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))

    if n < 0 or m < 0:
        raise ValueError("n и m должны быть неотрицательными")

    adj = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if not (0 <= u < n) or not (0 <= v < n):
            raise ValueError("В ребре вершина вне диапазона [0, n-1]")
        adj[u].append(v)
        adj[v].append(u)

    start = int(next(it))

    for i in range(n):
        adj[i].sort()

    order = bfs_order(n, adj, start)

    with open("output.txt", "w") as out:
        out.write(" ".join(map(str, order)))


if __name__ == "__main__":
    main()
