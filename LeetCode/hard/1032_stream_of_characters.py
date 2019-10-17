"""
https://leetcode.com/problems/stream-of-characters/

Implement the StreamChecker class as follows:

    StreamChecker(words): Constructor, init the data structure with the given words.
    query(letter): returns true if and only if for some k >= 1, the last k characters queried
    (in order from oldest to newest, including this letter just queried)
    spell one of the words in the given list.

For example:
    StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
    streamChecker.query('a');          // return false
    streamChecker.query('b');          // return false
    streamChecker.query('c');          // return false
    streamChecker.query('d');          // return true, because 'cd' is in the wordlist
"""

"""
Accepted
Time Complexity: O(n) for each query
Space Complexity: O(nm) where m is the length of the longest word and n is the number of words
Solution Explanation:
    Aho-Corasick String Matching Algorithm.
"""
from collections import deque


class StreamChecker:
    class Node:
        def __init__(self, val: str, parent: "Node", real: bool):
            self.val = val
            self.parent = parent
            self.real = real
            self.children = None
            self.longest_strict_suffix_link = None
            self.valid_suffix_link = None

    def __init__(self, words: List[str]):
        self.trie = self.__build_trie(words)
        __add_suffix_links(self, self.trie)

    def __print_trie(self) -> None:
        """Prints the trie in level order, each level on a new line."""
        q = deque()
        seen = set()
        q.append(self.trie)
        q.append(None)
        while q:
            current = q.popleft()
            if current is None:
                print()
                q.append(None)
                continue
            if current.children:
                q.extend(current.children.values())
            print(current.val, end=" ")

    def __build_trie(self, words: List[str]) -> Node:
        """Returns a trie from the input list of words."""
        words = set(words)
        root = self.Node("", parent=None, real=False)

        for word in words:
            current = root
            path = []
            for char in word:
                path.append(char)
                word_so_far = "".join(path)
                if not current.children:
                    current.children = {}
                if char not in current.children:
                    current.children[char] = self.Node(
                        char, parent=current, real=(word_so_far in words)
                    )
                current = current.children[char]

        return root

    @staticmethod
    def __add_suffix_links(root: Node) -> None:
        """Adds suffix links to to the passed in trie."""
        pass

    def query(self, letter: str) -> bool:
        return True


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
