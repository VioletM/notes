def bfs(g: dict) -> list:
    current_v = next(iter(g))
    queue_v = [*g[current_v]]
    marcked_v = set([current_v])
    path = [current_v]
    while len(queue_v) > 0:
        current_v = queue_v.pop(0)
        if current_v not in marcked_v:
            marcked_v.add(current_v)
            path.append(current_v)
            queue_v += [*g[current_v]]
    return path
