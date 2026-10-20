\# 85. Maximal Rectangle (Hard)



Link: https://leetcode.com/problems/maximal-rectangle/



\## Approach

Build a histogram of consecutive 1s for each row, then find the largest

rectangle in that histogram using a monotonic stack.



\## Complexity

\- Time: O(rows \* cols)

\- Space: O(cols)



\## Files

\- `solution.py` - histogram + monotonic stack

