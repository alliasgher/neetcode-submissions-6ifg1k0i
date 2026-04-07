class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(word, child):
            cur = child

            for i in range(len(word)):
                if word[i] == '.':
                    for child in cur.children.values():
                        if dfs(word[i+1:], child):
                            return True

                    return False

                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            if cur.isEnd:
                return True
            return False

        return dfs(word, self.root)
        
