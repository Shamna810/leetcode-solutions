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