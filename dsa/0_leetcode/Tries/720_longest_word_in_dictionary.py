from typing import List
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        check = self.root
        for letter in word:
            if letter not in check.children:
                check.children[letter] = Node()
            check = check.children[letter] 
        check.is_end = True
        
class Solution:
    def __init__(self):
        self.added_words = Trie()
        
    def longestWord(self, words: List[str]) -> str:
        self.best = ''
        for word in words:
            self.added_words.insert(word)
            
        def search_longest(node: Node, string_built: str):
            if (len(string_built) > len(self.best) or 
                (len(string_built) == len(self.best) and string_built < self.best)):
                self.best = string_built
                
            for child in node.children:
                nxt = node.children[child]
                if nxt.is_end == True:
                    search_longest(nxt, string_built+child)
            
        search_longest(self.added_words.root, '')
        
        return self.best