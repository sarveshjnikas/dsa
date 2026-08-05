from typing import List
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
        
        q = deque()
        q.append(beginWord)
        
        level = 0
        word_levels = {beginWord: 0}
        parents = {word: [] for word in wordList}
        
        while q:
            word  = q.popleft()
            for i in range(len(word)):
                for j in letters:
                    current_word = word[:i] + j + word[i+1:]
                    if current_word in parents and current_word != word: # we have it in word list
                        if current_word in word_levels: # we have built this word before.
                            current_level = word_levels[current_word]
                            proposed_level = word_levels[word] + 1
                            if proposed_level < current_level:
                                word_levels[current_word] = proposed_level
                                parents[current_word] = [word]
                                q.append(current_word)
                            elif proposed_level == current_level:
                                parents[current_word].append(word)
                        else: # we have never built this word.
                            word_levels[current_word] = word_levels[word] + 1
                            parents[current_word] = [word]
                            q.append(current_word)
        
            solutions = []

        def getchain(word, path):
            if word == beginWord:
                solutions.append([beginWord] + path[::-1])
                return

            for parent in parents[word]:
                path.append(word)
                getchain(parent, path)
                path.pop()

        if endWord not in parents or len(parents[endWord]) == 0:
            return []

        getchain(endWord, [])
        return solutions
        