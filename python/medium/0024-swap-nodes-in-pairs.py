# 24. Swap Nodes in Pairs (Medium)
# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Approach:
#   Use a dummy node before the head so swapping the first pair needs no
#   special case. For each pair (first, second) after `prev`, rewire three
#   pointers: prev -> second -> first -> rest. Then move prev to `first`,
#   which is now the tail of the swapped pair.
#
# Time:  O(n), each node is visited once
# Space: O(1), only a few pointers
#
# Edge cases: empty list, single node, odd length (last node stays put)

# 24. Swap Nodes in Pairs (Medium)
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Time: O(n)  Space: O(1)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # swap the pair by rewiring pointers
            first.next = second.next
            second.next = first
            prev.next = second

            # move to the end of the swapped pair
            prev = first

        return dummy.next