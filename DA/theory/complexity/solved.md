# Question 1
### Time Complexity Analysis

---

1.  **Shopping Cart Total**
    *   **linear n**, because we iterate through the prices once.

2.  **Vehicle Queue**
    *   **linear n**, each vehicle is processed once in the queue.

3.  **Call Center Support**
    *   **linear n**, because of two separate loops, each iterating over calls list once.

4.  **Employee Hierarchy Tree**
    *   **linear complexity**, because preorder traversal goes to each node in the tree once.

5.  **Social Network**
    *   **linear, O(V+E)**, where `V` is the number of people or vertices and `E` is the number of friendships or edges, because bfs visits every person and friends once.

6.  **Warehouse Inventory**
    *   **constant time O(1)** for lookups and inserting, because dict operations are O(1).

7.  **Hospital Patient Priority**
    *   **O(n log n)**. heapop is logarithmic because we replace the popped node with the rightmost node and then move it to its correct position, which in worst case could have to moved down to leaf, so height of tree in other words which is logn). heapify is linear so we get n * logn.

8.  **Text Word Frequency**
    *   **O(n log n)**. Making the frequency map is linear, sorting the `k` unique words takes `O(k log k)` and in the worst case, `k` could be `n`.



<br>
<br>

# Question 2
### Space Complexity Analysis

---

1.  **Parentheses Checker**
    *   `mapping` is constant space. The `stack` can grow atmost to the same size as the `expr` itself, so the final space complexity is **O(n)**.

2.  **Task Processing**
    *   The `queue` has the list of tasks, so it is **linear space, O(n)**.

3.  **Hash Map Frequency Counter**
    *   All numbers can be unique, so the `hash` will have the same length as the input array. This is **linear space, O(n)**.

4.  **String Permutations**
    *   The callstack will grow to atmost `n` before returning. However, the `result` list will be `n * n!` after the function is done, as it needs to store the `n!` such arrangements, each of length `n`.

5.  **Longest Common Subsequence**
    *    Space required is **O(n * m)** for the 2D dp array.

6.  **BFS Traversal**
    *   The `visited` set and the `queue` can have all nodes of the graph in the worst case. So the space complexity is **O(V)**.

7.  **Fibonacci**
    *   The space is **linear, O(n)**, for the 1D DP array.

8.  **Binary Search Tree**
    *   The space to store `n` nodes in the tree is **O(n)**.
    *   For `insert`, the callstack may need to go from the root to a leaf, so the nodes needed for the callstack would be the max height of the tree.
    *   For `inorder` traversal, the logic is same, the callstack can grow to the max height.
    *   Since the tree could be skewed if we insert in sorted order (like a linked list), the height would be `n`.
    *   So, `insert` and `inorder` take **O(n)** space in the worst case due to recursion depth.




<br>
<br>


# Question 3

### Game 1

---

#### Script 1

##### Time Complexity
*   `len(word)` for initial random choice and `len`.
*   Linear `O(k)` for `guess in guesses` check.
*   Constant for `append`.
*   `len(word)` for `guess not in word` check.
*   Checking matches: `len(word) * len(guessed)` which is `O(m*k)`.
*   Checking for `_`: `O(m)` or `len(word)`.
*   **Total:** `(m*k + m) * tries`

##### Space Complexity
*   `len(words)` for the initial list.
*   `len(word)` for the `display` string.
*   `tries` for the `guesses` list.
*   **Total:** `O(m + k)`

---

#### Script 2

##### Time Complexity
*   `len(word)` for initial random choice and for `len`.
*   `check for if guessed` is constant `O(1)` because it's a set.
*   Constant for adding to the set.
*   `len(word)` for `if guess in word` check.
*   Checking for `_`: `O(m)` or `len(word)`.
*   **Total:** `O(m) * tries`

##### Space Complexity
*   `len(word)` for the words list.
*   `revealed` list is `len(word)`.
*   `guessed_letters` set will be at most `k` or number of tries.
*   **Total:** `O(m + k)`

---

#### Decision for Game 1
Script 2 is the better choice. Its time complexity `O(m)` is much better than Script 1's `O(m*k)`.

<br>


### Game 2

---

#### Script 1

> **What's it doing?**
> This script takes in a string (hardcoded here), and checks if the string exists as a connected path in any direction. We run dfs on every cell, and if for any cell, we have the entire string as a path in any direction without any breaks, then we return true to state that it exists.

##### Time Complexity
We run this dfs on every single cell in the grid, so this gives `r*c` times the dfs cost. In the dfs call for a cell, we again run dfs on its top, bottom, left, and right neighbours. Since we don't know where the path could be for the string, we check all 4 paths. This path can go at most `len(word)` far. In each of these new 4 calls, we make 4 new calls for each, and so on. For the 3rd character, we'd be exploring `4^3=64` paths. We need to check till the last character, so it goes till `len(word)`.
*   **Total:** `O(r * c * 4^len(word))`

##### Space Complexity
The callstack can grow at most to the length of the longest path, which is `len(word)`, since dfs completes the current path before moving on to the next from where it started.
*   **Total:** `O(len(word))`

---

#### Script 2

> **What's it doing?**
> A trie is basically a way to store strings in the form of a tree using nodes for each character of a string in a sequence. For example, if we inserted 'CAT', we would make a node for C, then make A its child, then make T a child of A, like: `root -> C -> A -> T(end=True)`.
>
> Like before, we run dfs on each of the `r*c` cells. But this time, we first make a trie of the word(s). In each call, instead of checking the current index of a single string, we check if the current cell's character can continue the current node of the trie. If yes, it means at least one word's path has matched so far, and we continue going further to its children.

##### Time Complexity
1.  **Trie Building:** For building the trie, we insert each word character by character. For inserting `n` words, it would take `O(sum of lengths of all words)`.
2.  **dfs Search:** The logic is the same as Script 1, but the search depth is limited by the longest word.
*   **Total:** `O(sum of lengths of words + r * c * 4^LMAX)` where `LMAX` is the max length of a word.

##### Space Complexity
1.  **Trie Storage:** The space for the trie is the number of nodes created, which in the worst case is `O(sum of lengths of all words)`.
2.  **dfs Callstack:** The callstack will grow at most to the longest word's length.
*   **Total:** `O(sum of lengths of all words + LMAX)`

---

#### Decision for Game 2
Overall, Script 2 is the better choice. If we had `N` words, Script 1 would take `O(N * r * c * 4^LMAX)` time, compared to Script 2 which takes `O(S + r * c * 4^LMAX)`. However, there is a tradeoff because we need the extra space to store the Trie in Script 2.