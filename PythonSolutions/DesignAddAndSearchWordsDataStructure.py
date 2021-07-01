class TrieNode():
    def __init__(self):
        self.children = {}
        self.endWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endWord = True

    def searchNode(self, node, word):
        for i, char in enumerate(word):
            if char == ".":
                # checks if end of word
                if i == len(word) - 1:
                    for x in node.children.values():
                        if x.endWord:
                            return True
                    return False
                # if not end of word
                for childNode in node.children.values():
                    if self.searchNode(childNode, word[i + 1:]):
                        return True
                return False
            else:
                if char in node.children:
                    node = node.children[char]
                else:
                    return False
        if node.endWord:
            return True
        return False

    def search(self, word: str) -> bool:
        node = self.root
        return self.searchNode(node, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)