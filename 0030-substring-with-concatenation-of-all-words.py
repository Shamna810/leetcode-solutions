from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        w = len(words[0])        # length of each word
        n = len(words)           # number of words
        need = Counter(words)    # required count of each word
        res = []

        for offset in range(w):
            left = offset
            count = 0            # number of valid words in the window
            seen = Counter()     # words currently in the window

            for right in range(offset, len(s) - w + 1, w):
                word = s[right:right + w]

                if word in need:
                    seen[word] += 1
                    count += 1

                    # too many copies of this word: shrink from the left
                    while seen[word] > need[word]:
                        seen[s[left:left + w]] -= 1
                        left += w
                        count -= 1

                    # window has exactly all the words
                    if count == n:
                        res.append(left)
                        seen[s[left:left + w]] -= 1
                        left += w
                        count -= 1
                else:
                    # invalid word: reset the window
                    seen.clear()
                    count = 0
                    left = right + w

        return res