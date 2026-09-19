# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            v1 = list1.val
            v2 = list2.val
            if v1 < v2:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy.next

'''
建立一个虚拟头结点，然后使用两个指针遍历两个链表，比较当前节点的值，将较小的节点连接到结果链表的尾部。
继续移动指针，直到其中一个链表遍历完。最后将未遍历完的链表连接到结果链表的尾部。
'''
