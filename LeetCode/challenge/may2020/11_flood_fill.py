"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/

An image is represented by a 2-D array of integers, each integer representing the pixel
value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood
fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the
starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those
pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the
aforementioned pixels with the newColor.

At the end, return the modified image.
"""

"""
Accepted
Time complexity: O(n^2) where n^2 is the number of pixels
Space complexity: O(n^2) as we recurse on each pixel that matches our source pixel's color
"""


class Solution:
    def _flood(self, image, x, y, originalColor, newColor) -> None:
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or image[x][y] != originalColor:
            return
        image[x][y] = newColor # I change it first to the flag, -1, to mark that pixel as visited.
        self._flood(image, x - 1, y, originalColor, newColor)
        self._flood(image, x + 1, y, originalColor, newColor)
        self._flood(image, x, y - 1, originalColor, newColor)
        self._flood(image, x, y + 1, originalColor, newColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        image[sr][sc] = -1 # -1 is a flag to mark a changed pixel so that we dont infinitely recurse.
        self._flood(image, sr - 1, sc, originalColor, -1)
        self._flood(image, sr + 1, sc, originalColor, -1)
        self._flood(image, sr, sc - 1, originalColor, -1)
        self._flood(image, sr, sc + 1, originalColor, -1)
        return [[i if i != -1 else newColor for i in row] for row in image]
