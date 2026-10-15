\# 3. Longest Substring Without Repeating Characters



\*\*Difficulty:\*\* Medium

\*\*Link:\*\* https://leetcode.com/problems/longest-substring-without-repeating-characters/



\## Problem

Given a string `s`, find the length of the longest substring without duplicate characters.



\## Examples

| Input | Output | Explanation |

|-------|--------|-------------|

| `"abcabcbb"` | 3 | `"abc"` |

| `"bbbbb"` | 1 | `"b"` |

| `"pwwkew"` | 3 | `"wke"` (a substring, not the subsequence `"pwke"`) |



\## Constraints

\- `0 <= s.length <= 5 \* 10^4`

\- `s` consists of English letters, digits, symbols and spaces.



\## Approach

Sliding window with a hash map storing each character's last seen index.

When a duplicate is found inside the window, move the left pointer past

its previous position.



\## Complexity

\- Time: O(n)

\- Space: O(min(n, m)) where m is the charset size

