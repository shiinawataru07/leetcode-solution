# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        l1, l2 = 0, 0
        while p1:
            p1 = p1.next
            l1 += 1
        while p2:
            p2 = p2.next
            l2 += 1
        p1, p2 = headA, headB
        for _ in range(l1 - l2):
            p1 = p1.next
        for _ in range(l2 - l1):
            p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


'''
先遍历一遍得到链表A和链表B的长度，然后让长的链表先走差值步数，这样两个指针就能同时到达相交点或者同时到达链表末尾。
时间复杂度 O(m+n) 空间复杂度 O(1)
'''
