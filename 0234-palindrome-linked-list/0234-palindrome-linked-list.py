# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        current_node = head
        nums = []
        # 연결 리스트를 리스트로 변환
        while current_node:
            nums.append(current_node.val)
            current_node = current_node.next

        return nums == nums[::-1]
        