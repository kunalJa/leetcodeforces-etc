package LeetCode.easy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Set;
import java.util.HashSet;

/*
 * Take a number, invert it, and then add it back to the original number.
 * If the number has any duplicate digits, repeat this process.
 *  Example:
 *      Input: 122
 *        122 + 221 = 343
 *        343 + 343 = 686
 *        686 + 686 = 1372
 *      Output: 3 1372
 */
public class JP_Morgan_Chase_Unique_Digits {

  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    while ((line = in.readLine()) != null) {
      System.out.println(noMoreDupes(Integer.parseInt(line)));
    }
  }
  
  /**
   * Returns the number of iterations and the value such that we added the
   * reverse of a number to itself until the number had no more duplicate digits.
   * This function always adds the reverse to the input the first time so the
   * minimum number of iterations it can return is 1. Even if the input had no
   * duplicate digits, it will do this first iteration.
   */
  private static String noMoreDupes(int current) {
      int i = 1;
      current += reverseDigits(current);
      while (duplicates(current)) {
          current += reverseDigits(current);
          i++;
      }
      return i + " " + current;
  }
  
  /**
   * Returns true if any digit in the number is a duplicate of the other digits.
   * This function ignores the input's sign.
   */
  private static boolean duplicates(int in) {
      in = Math.abs(in);
      int current;
      Set<Integer> digits = new HashSet<>();
      while (in > 0) {
          current = in % 10;
          if (digits.contains(current)) {
              return true;
          }
          digits.add(current);
          in /= 10;
      }
      return false;
  }
  
  /**
   * Returns an integer that has the digits reversed of the input n.
   * Input x keeps its sign, just has its digits reversed.
   */
  private static int reverseDigits(int x) {
      boolean negative = x < 0 ? true : false;
      x = Math.abs(x);
      int val = 0;
      while (x > 0) {
          val *= 10;
          val += x % 10;
          x /= 10;
      }
      if (negative) {
          return val * -1;
      }
      return val;
  }
}
