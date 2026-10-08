def bellman(v, e, edges, start):
    dist = [float("inf")]*(v+1) # 1 indexed
    dist[start] = 0

    for _ in range(v-1):
        updt = False

        for x, y, cost in edges:
            if dist[x] == float("inf"):
                continue

            new_cost = dist[x] + cost
            if new_cost < dist[y]:
                updt = True
                dist[y] = new_cost

        if not updt: break

    neg_cycle = False
    for x, y, cost in edges:
        if dist[x] != float("inf"):
            if dist[x] + cost < dist[y]:
                neg_cycle = True
                break

    return dist, neg_cycle