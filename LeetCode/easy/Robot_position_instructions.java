/*
 * Accepted
 * Time Complexity : O(n).
 * Space Complexity : O(1).
 */

/**
 * Given a list of commands, move the Roomba to that tiled position in a 2D grid.
 * The position of a tile in the grid is (row * matrixSize) + column.
 * The grid is zero indexed.
 * 
 * Don't forget Roomba's can't got through walls!
 *  Example:
 *  Input: 4 [RIGHT, LEFT, LEFT, DOWN]
 *  Output: 4
 *  
 *  Example:
 *  Input: 4 [RIGHT, RIGHT, DOWN, DOWN, DOWN, LEFT]
 *  Output: 9
 */

package LeetCode.easy;

import java.util.List;

public class Robot_position_instructions {
    static int roverMove(int matrixSize, List<String> cmds) {
        int cell = 0;
        for (String s : cmds) {
            if (s.toUpperCase().equals("RIGHT")) {
                if (cell % matrixSize != matrixSize - 1)
                    cell++;
            } else if (s.toUpperCase().equals("LEFT")) {
                if (cell % matrixSize != 0)
                    cell--;
            } else if (s.toUpperCase().equals("UP")) {
                if (cell >= matrixSize)
                    cell -= matrixSize;
            } else if (s.toUpperCase().equals("DOWN")) {
                if (cell < (matrixSize * (matrixSize - 1)))
                    cell += matrixSize;
            }
        }   
        return cell;
    }
}
