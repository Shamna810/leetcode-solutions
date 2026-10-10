# 23. Merge k Sorted Lists (Hard)
# https://leetcode.com/problems/merge-k-sorted-lists/
#
# Approach: min-heap holding the current head of each list.
# Pop the smallest node, append it to the result, push its next node.
# Time: O(N log k), Space: O(k), where N = total nodes, k = number of lists

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