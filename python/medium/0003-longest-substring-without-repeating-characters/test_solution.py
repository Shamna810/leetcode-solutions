from solution import Solution
from solution_v2 import Solution as SolutionV2

CASES = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("dvdf", 3),
    ("abba", 2),
]

def test_both_solutions():
    for sol in (Solution(), SolutionV2()):
        for s, expected in CASES:
            assert sol.lengthOfLongestSubstring(s) == expected, (s, expected)

if __name__ == "__main__":
    test_both_solutions()
    print("All tests passed")