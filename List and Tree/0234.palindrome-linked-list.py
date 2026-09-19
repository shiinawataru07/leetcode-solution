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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        quick, slow = head, head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
        newHead = self.reverseList(slow)
        cur = head
        while newHead:
            if cur.val != newHead.val:
                return False
            cur = cur.next
            newHead = newHead.next
        return True
'''
使用快慢指针找到链表的中点，然后反转后半段链表，最后逐个比较前半段和反转后的后半段是否相等。

当链表长度为奇数时，快慢指针结束后 `slow` 停在第 $(n+1)/2$ 个结点上；当链表长度为偶数时，快慢指针结束后 `slow` 停在第 $n/2 + 1$ 个结点上。
'''
