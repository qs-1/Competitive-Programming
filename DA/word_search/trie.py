class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

def find_words(board, words):
    trie = Trie()
    for w in words:
        trie.insert(w)
    result = set()
    rows, cols = len(board), len(board[0])

    def dfs(r, c, node, path):
        if node.end:
            result.add(path)
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children:
            return
        
        ch = board[r][c]
        board[r][c] = '#'
        next_node = node.children[ch]

        dfs(r+1, c, next_node, path + ch)
        dfs(r-1, c, next_node, path + ch)
        dfs(r, c+1, next_node, path + ch)
        dfs(r, c-1, next_node, path + ch)

        board[r][c] = ch  # backtrack

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root, "")

    return list(result)


board = [
    ['C', 'A', 'T'],
    ['R', 'A', 'T'],
    ['D', 'O', 'G']
]
words = ["CAT", "DOG", "COW"]
print("Found Words:", find_words(board, words))
