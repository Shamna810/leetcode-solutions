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

class Solution2:
    """Divide and conquer: merge lists pairwise until one remains."""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwo(l1, l2))
            lists = merged

        return lists[0]

    def mergeTwo(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next