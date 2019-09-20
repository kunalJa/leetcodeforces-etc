"""
https://leetcode.com/problems/defanging-an-ip-address/

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    Iterate through the string adding each character to a new list.
    If the character is a ".", add a "[.]" to the list instead of the character.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join([c if c != "." else "[.]" for c in address])
