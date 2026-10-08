import heapq

def dijkstra(adj_list, start, end, n, blen, a, b):
    dist = [float('inf')]*n
    dist[start] = 0
    parent = [-1]*n
    operation = [None]*n
    
    pq = [(0,start)]
    
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue
        if u==end:
            break
        
        for v, cost in adj_list[u]:
            new_dist = dist[u] + cost
            
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                
                i1 = u//(blen+1)
                j1 = u%(blen+1)
                i2 = v//(blen+1)
                j2 = v%(blen+1)
                
                if i2==i1 + 1 and j2==j1 + 1:
                    if a[i1]==b[j1]:
                        operation[v] = f"Match '{a[i1]}'"
                    else:
                        operation[v] = f"Substitute '{a[i1]}' with '{b[j1]}'"
                elif i2==i1 and j2==j1 + 1:
                    operation[v] = f"Insert '{b[j1]}'"
                elif i2==i1 + 1 and j2==j1:
                    operation[v] = f"Delete '{a[i1]}'"
                
                heapq.heappush(pq, (new_dist, v))
    
    transcript = []
    curr = end
    while parent[curr] != -1:
        transcript.append(operation[curr])
        curr = parent[curr]
    
    return dist[end], transcript[::-1]

def edist_adj_list(a, b):
    alen = len(a)
    blen = len(b)
    n = (alen+1)*(blen+1)
    
    adj_list = {i: [] for i in range(n)}
    
    for i in range(alen+1):
        for j in range(blen+1):
            curr_node = i * (blen+1) + j
            
            if i<alen and j<blen:
                next_node = (i+1) * (blen+1) + (j+1)
                if a[i]==b[j]:
                    adj_list[curr_node].append((next_node, 0))  # same
                else:
                    adj_list[curr_node].append((next_node, 1))  # subst
            
            if j<blen:
                next_node = i * (blen+1) + (j+1)
                adj_list[curr_node].append((next_node, 1))  # insert
            
            if i<alen:
                next_node = (i+1) * (blen+1) + j
                adj_list[curr_node].append((next_node, 1))  # del
    
    start = 0
    end = alen*(blen+1) + blen
    min_dist, transcript = dijkstra(adj_list, start, end, n, blen, a, b)
    return min_dist, transcript


# Test case 1
print("=" * 50)
print("Test case 1: 'rat' → 'cat'")
print("=" * 50)
a = "rat"
b = "cat"
dist, transcript = edist_adj_list(a, b)
print(f"Edit distance: {dist}\n")
for step in transcript:
    print(f"  {step}")

# Test case 2
print("\n" + "=" * 50)
print("Test case 2: 'kitten' → 'sitting'")
print("=" * 50)
a = "kitten"
b = "sitting"
dist, transcript = edist_adj_list(a, b)
print(f"Edit distance: {dist}\n")
for step in transcript:
    print(f"  {step}")

# Test case 3
print("\n" + "=" * 50)
print("Test case 3: 'hello' → 'hello'")
print("=" * 50)
a = "hello"
b = "hello"
dist, transcript = edist_adj_list(a, b)
print(f"Edit distance: {dist}\n")
for step in transcript:
    print(f"  {step}")