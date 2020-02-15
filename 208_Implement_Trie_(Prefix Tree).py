# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for ch in word:
            if ch not in trie:
                trie[ch] = {}
            trie = trie[ch]

        trie["end"] = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for ch in word:
            if ch not in trie:
                return False
            trie = trie[ch]

        if "end" in trie:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for ch in prefix:
            if ch not in trie:
                return False
            trie = trie[ch]

        return True
