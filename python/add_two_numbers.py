# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        has_carry = False
        loop_count = 0
        prev_node = None
        head_node = None
        
        while l1 is not None or l2 is not None or has_carry:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            sum_val = l1_val + l2_val
            
            if has_carry:
                sum_val += 1
                has_carry = False
            if sum_val > 9:
                sum_val = sum_val % 10 #Get the last digit
                has_carry = True
                
            l3_node = ListNode(val=sum_val)
            
            if loop_count == 0:
                head_node = l3_node
                prev_node = head_node
            elif loop_count > 0:
                prev_node.next = l3_node
                prev_node = l3_node
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
            loop_count += 1
            
        return head_node
            
            
