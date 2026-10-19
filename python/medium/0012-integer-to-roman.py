# LeetCode 12: Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

# Difficulty: Medium
#
# Approach: Greedy. Go through values from largest to smallest,
# including subtractive forms (900, 400, 90, 40, 9, 4), and subtract
# each as many times as it fits.
#
# Time: O(1) | Space: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []
        for value, symbol in zip(values, symbols):
            if num == 0:
                break
            count, num = divmod(num, value)
            result.append(symbol * count)

        return "".join(result)