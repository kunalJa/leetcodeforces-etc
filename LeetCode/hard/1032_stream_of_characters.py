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
        def __init__(self, val: str, parent: "Node", real: bool, path: str):
            self.val = val
            self.parent = parent
            self.real = real
            self.path = path
            self.children = {}
            self.longest_strict_suffix_link = None
            self.valid_suffix_link = None

    def __init__(self, words: List[str]):
        self.trie = self.__build_trie(words)
        StreamChecker.__add_suffix_links(self.trie)
        self.current = self.trie

    @staticmethod
    def __print_trie(root: Node) -> None:
        """Prints the trie in level order, each level on a new line."""
        q = deque()
        q.append(root)
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
        root = self.Node("", parent=None, real=False, path="")

        for word in words:
            current = root
            path = []
            for char in word:
                path.append(char)
                word_so_far = "".join(path)
                if char not in current.children:
                    current.children[char] = self.Node(
                        char,
                        parent=current,
                        real=(word_so_far in words),
                        path=word_so_far,
                    )
                current = current.children[char]

        return root

    @staticmethod
    def __add_suffix_links(root: Node) -> None:
        """
        Adds suffix links to to the passed in trie.
        The blue arcs can be computed in linear time by repeatedly traversing the blue arcs until
        the traversing node has a child matching the character of the target node.
        """
        q = deque()
        q.append(root)
        while q:
            current = q.popleft()
            parent = current.parent
            while parent and not current.longest_strict_suffix_link:
                blue_link = parent.longest_strict_suffix_link
                if blue_link:
                    if current.val in blue_link.children:
                        current.longest_strict_suffix_link = blue_link.children[
                            current.val
                        ]
                else:
                    current.longest_strict_suffix_link = parent
                parent = blue_link

            q.extend(current.children.values())

        q.append(root)
        while q:
            current = q.popleft()
            blue_link = current.longest_strict_suffix_link
            while blue_link and not current.valid_suffix_link:
                if blue_link.real:
                    current.valid_suffix_link = blue_link
                elif blue_link.valid_suffix_link:
                    current.valid_suffix_link = blue_link.valid_suffix_link

                blue_link = blue_link.longest_strict_suffix_link

            q.extend(current.children.values())

    def query(self, letter: str) -> bool:
        if letter in self.current.children:
            self.current = self.current.children[letter]
        else:
            while self.current.longest_strict_suffix_link:
                if letter in self.current.children:
                    self.current = self.current.children[letter]
                    break

                self.current = self.current.longest_strict_suffix_link

            if self.current.val != letter:
                if letter in self.current.children:
                    self.current = self.current.children[letter]

        return self.current.real or self.valid_suffix_link


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
