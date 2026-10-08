def dijkstra(adj, start, v):
    dist = [float("inf")]*(v+1) # 1 indexed
    dist[start] = 0

    pq = [(0,start)] 

    while pq:
        currcost, u = heapq.heappop(pq) 

        if currcost > dist[u]:
            continue

        for cost, v in adj[u]: 
            newcost = currcost + cost

            if newcost < dist[v]:
                dist[v] = newcost
                heapq.heappush(pq, (newcost, v))

    return dist