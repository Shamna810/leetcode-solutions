# 23. Merge k Sorted Lists (Hard)
# https://leetcode.com/problems/merge-k-sorted-lists/
#
# Problem: merge k sorted linked lists into one sorted linked list.
#
# Approach 1 (Solution): Min-heap
#   - Put the head of every list into a min-heap.
#   - Pop the smallest node, attach it to the result, push its next node.
#   - The tuple (val, i, node) uses i as a tie-breaker so Python never
#     has to compare two ListNode objects.
#   Time: O(N log k)   Space: O(k)
#
# Approach 2 (Solution2): Divide and conquer
#   - Merge lists in pairs, repeat until one list remains.
#   Time: O(N log k)   Space: O(1) extra (besides the list of lists)
#
# N = total number of nodes, k = number of lists


import heapq
from typing import List, Optional


# Definition for singly-linked list (provided by LeetCode).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                # i is a tie-breaker so Python never compares two ListNodes
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next