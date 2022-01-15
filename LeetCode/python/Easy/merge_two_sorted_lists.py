from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = Solution.mergeTwoLists(self, list1.next, list2)
        return list1 or list2

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 is None and list2 is None:
#             return None
#         if list1 is None:
#             return list2
#         if list2 is None:
#             return list1
#
#         if list1.val < list2.val:
#             list1.next = Solution.mergeTwoLists(self, list1.next, list2)
#             return list1
#         else:
#             list2.next = Solution.mergeTwoLists(self, list1, list2.next)
#             return list2


ls1 = ListNode(-9, ListNode(3))
ls2 = ListNode(5, ListNode(7))

sol = Solution()
b = sol.mergeTwoLists(ls1, ls2)
print(b.next.next.val)