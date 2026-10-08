import heapq

def dijkstra(adj_matrix, start, end, n, blen, a, b):
    dist = [float('inf')]*n
    dist[start] = 0
    parent = [-1]*n
    ops = [None]*n
    
    pq = [(0,start)]
    
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue
        if u == end:
            break
        
        for v in range(n):
            if adj_matrix[u][v] != float('inf'):
                new_dist = dist[u] + adj_matrix[u][v]
                
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
                    
                    i1 = u//(blen+1)
                    j1 = u%(blen+1)
                    i2 = v//(blen+1)
                    j2 = v%(blen+1)
                    
                    if i2==i1+1 and j2==j1+1:
                        if a[i1]==b[j1]:
                            ops[v] = f"Match '{a[i1]}'"
                        else:
                            ops[v] = f"Substitute '{a[i1]}' with '{b[j1]}'"
                    
                    elif i2==i1 and j2==j1+1:
                        ops[v] = f"Insert '{b[j1]}'"
                    
                    
                    elif i2==i1 + 1 and j2==j1:
                        ops[v] = f"Delete '{a[i1]}'"
                    
                    heapq.heappush(pq, (new_dist, v))
    
    transcript = []
    curr = end
    while parent[curr] != -1:
        transcript.append(ops[curr])
        curr = parent[curr]
    
    return dist[end], transcript[::-1]



def edist_adj_matrix(a, b):
    alen = len(a)
    blen = len(b)
    n = (alen+1)*(blen+1)
    
    adj_matrix = [[float('inf')] * n for _ in range(n)]
    
    for i in range(alen+1):
        for j in range(blen+1):
            curr_node = i * (blen+1) + j
            
            if i<alen and j<blen:
                next_node = (i+1) * (blen+1) + (j+1)
                if a[i] == b[j]:
                    adj_matrix[curr_node][next_node] = 0
                else:
                    adj_matrix[curr_node][next_node] = 1
            
            if j<blen:
                next_node = i * (blen+1) + (j+1)
                adj_matrix[curr_node][next_node] = 1
            
            if i<alen:
                next_node = (i+1) * (blen+1) + j
                adj_matrix[curr_node][next_node] = 1
    
    start = 0
    end = alen*(blen+1) + blen
    min_dist, transcript = dijkstra(adj_matrix, start, end, n, blen, a, b)
    
    return min_dist, transcript


