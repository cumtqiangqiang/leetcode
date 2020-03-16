'''

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

'''


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		i = head
		for t in range(n):
			i = i.next

		# if i is none,remove head
		if i is None:
			head = head.next
			return head
		j = head  # j is n+1 step behind i

		# move i to the end,j follow i with n+1 step behind
		while i.next is not None:
			i = i.next
			j = j.next
		j.next = j.next.next  # remove j.next
		return head


if __name__ == '__main__':
	n5 = ListNode(5)
	n4 = ListNode(4)
	n3 = ListNode(3)
	n2 = ListNode(2)
	n1 = ListNode(1)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n = n1
	print(n.val)
	while n.next is not  None:
		n = n.next
		print(n.val)

	s = Solution()
	res = s.removeNthFromEnd(n1,2)
	# print(res)



