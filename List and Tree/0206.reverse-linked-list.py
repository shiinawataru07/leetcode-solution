# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
'''
迭代法：使用三个指针，一个指向当前节点，一个指向当前节点的前一个节点，一个指向当前节点的后一个节点。遍历链表，将每个节点的next指针指向前一个节点。
递归法：递归地反转链表的后半部分，然后将当前节点的next指针指向前一个节点。
时间复杂度 O(n) 空间复杂度 O(1)
'''
