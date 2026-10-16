# 24. Swap Nodes in Pairs - Recursive approach
# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Approach:
#   Swap the first two nodes, then recursively solve the rest of the list
#   and attach the result.
#
# Time:  O(n)
# Space: O(n), recursion stack (iterative version uses O(1))

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second