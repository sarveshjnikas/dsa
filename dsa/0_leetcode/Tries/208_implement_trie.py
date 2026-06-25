class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        check = self.root
        for letter in word:
            if letter not in check.children:
                check.children[letter] = Node()
            check = check.children[letter]
        check.is_end = True
        return None
        

    def search(self, word: str) -> bool:
        check = self.root
        for letter in word:
            if letter not in check.children:
                return False
            check = check.children[letter]
        return check.is_end
        

    def startsWith(self, prefix: str) -> bool:
        check = self.root
        for letter in prefix:
            if letter not in check.children:
                return False
            check = check.children[letter]
        return True
        
        
