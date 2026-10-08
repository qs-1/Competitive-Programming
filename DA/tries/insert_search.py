class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True



def edist_trie(a, words):
    #add all words to trie
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    ans = {}
    alen = len(a)
    def dfs(node, prev_col, currword):
        if node.end: #end, result found for this word
            ans[currword] = prev_col[alen]
        
        for char_b, child in node.children.items():
            curr_column = [0]*(alen+1)
            curr_column[0] = prev_col[0]+1
            
            for i in range(1, alen + 1):
                char_a = a[i-1]
                
                if char_a == char_b:
                    curr_column[i] = prev_col[i-1]
                else:
                    insert = curr_column[i-1]
                    delete = prev_col[i]
                    replace = prev_col[i-1]
                    curr_column[i] = 1 + min(insert, delete, replace)
            
            dfs(child, curr_column, currword + char_b)
    
    basecase = [i for i in range(alen+1)]
    dfs(trie.root, basecase, "")
    return ans
