# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode(0)
        cur = res
        while l1 or l2 or carry :
            if l1 :
                carry += l1.val
                l1 = l1.next
            if l2 :
                carry += l2.val
                l2 = l2.next
            cur.val = carry % 10
            carry //= 10
            if l1 or l2 or carry :
                cur.next = ListNode(0)
                cur = cur.next
        return res


'''
解析：
对两个链表进行求和，carry记载每位所处理的和
在循环当中，只有接下来还要创建新的位数再创建新的listnode，否则会出现前导0
参考cpp的高精度加法实现
'''
