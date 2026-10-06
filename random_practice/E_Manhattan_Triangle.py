from collections import defaultdict
import bisect

def possible_C_choices(x,y):
    # check if any valid corner point exists
    # (lies halfway on the 4 sides of
    #  manhattan diamond of A)
    half = d/2
    possible = [(x-half, y+half),
                (x+half, y+half),
                (x-half, y-half),
                (x+half, y-half)]
    
    # check for existence
    found = []
    for p in possible:
        if p in pointset:
            found.append(p)
    return found

def solve():
    diag_left = defaultdict(list)
    diag_right = defaultdict(list)

    coord_idx = {}

    global pointset
    pointset = set()
    for i in range(n):
        # read point
        x, y = list(map(int, input().split()))
        pointset.add((x,y))
        coord_idx[(x,y)] = i+1

        # link the diagonal ids with the points that pass through it
        diag_left[x+y].append(x) # \ (slope -1)
        diag_right[x-y].append(x) # / (slope +1)

    # sort these points so we can binary search to find 3rd point
    for key in diag_left:
        diag_left[key].sort()
    for key in diag_right:
        diag_right[key].sort()
    
    # now for each point A, we know if its the ans, C will
    # lie on one of the midpoints of its manhattan diamond
    # and final point B will lie on the intersection of the
    # diamonds of A and C (this intersection part is where
    # b should lie)
    for a in pointset:
        C_choices = possible_C_choices(*a)
        
        # now to search for B, we first need to know where
        # the A-C intersection diagonal is

        for c in C_choices:
            if (a[0] <= c[0]) == (a[1] <= c[1]): # both true \, both false, still \ (edge on which c lies)
                # now b lies on right diagonal / of A, it may be on the right half segment
                # or left half segment
                diag_id_a = a[0]-a[1]
                for dist in [-d, d]:
                    possible_id_b = diag_id_a + dist
                    if possible_id_b not in diag_right:
                        continue
                    
                    points_on_diag = diag_right[possible_id_b]

                    min_x = min(a[0], c[0]) + dist/2
                    max_x = max(a[0], c[0]) + dist/2

                    #binary search to find B within min max segment
                    found = bisect.bisect_left(points_on_diag, min_x)
                    if found<len(points_on_diag) and points_on_diag[found]<=max_x:
                        bx = points_on_diag[found]
                        by = bx - possible_id_b #(rearranging x-y = id)
                        b = (bx,by)
                        print(coord_idx[a],coord_idx[b],coord_idx[c])
                        return
            else: # both / cases
                diag_id_a = a[0]+a[1]
                for dist in [-d, d]:
                    possible_id_b = diag_id_a + dist
                    if possible_id_b not in diag_left:
                        continue
                    
                    points_on_diag = diag_left[possible_id_b]

                    min_x = min(a[0], c[0]) + dist/2
                    max_x = max(a[0], c[0]) + dist/2

                    found = bisect.bisect_left(points_on_diag, min_x)
                    if found<len(points_on_diag) and points_on_diag[found]<=max_x:
                        bx = points_on_diag[found]
                        by = possible_id_b - bx #(rearranging x+y = id)
                        b = (bx,by)
                        print(coord_idx[a],coord_idx[b],coord_idx[c])
                        return
    print(0,0,0)


cases = int(input())
for _ in range(cases):
    n, d = list(map(int, input().split()))
    solve()    























    