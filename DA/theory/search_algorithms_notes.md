1. A* (A-Star) Search
Uses a priority queue to explore nodes based on the sum of actual cost from start and estimated cost to goal. It prioritizes paths that look most promising according to given heuristic so it finds the optimal path faster than other search algorithms.

2. Minimax Algorithm
recursively explores the game tree by alternating between maximizing and minimizing players. The maximizer tries to pick the move with the highest score, while the minimizer picks the lowest.

3. Uniform Cost Search (UCS)
explores nodes in order of their cumulative cost from the start using a pq. always visits the cheapest node next, so it guarantees finding the path with the lowest total cost. 

4. Iterative Deepening Search (IDS)
does depth limited dfs with increasing depth limits. It starts at depth 0 then 1, then 2 and so on until the goal is found. It redoes work at shallower depths but the overhead is not that bad cuz most nodes are at deeper levels.