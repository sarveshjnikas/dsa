class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        check = self.root
        for letter in word:
            if letter not in check.children:
                check.children[letter] = Node()
            check = check.children[letter]
        check.is_end = True
        

    def search(self, word: str) -> bool:
        def _search(node, word):
            if not word:
                return True if node.is_end else False

            if word[0] == ".":
                ans = False
                for child in node.children:
                    ans = ans or _search(node.children[child], word[1:])
                return ans
            else:
                if word[0] not in node.children:
                    return False
                return _search(node.children[word[0]], word[1:])

        return _search(self.root, word)