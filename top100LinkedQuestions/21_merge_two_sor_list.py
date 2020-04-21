class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> None:
		res = ListNode(0)
		tail = res
		while(l1 and l2):
			if (l1.val < l2.val):
				tail.next = l1
				l1 = l1.next
			else:
				tail.next = l2
				l2 = l2.next
			tail = tail.next

		if (l1):tail.next = l1
		if (l2):tail.next = l2
		return res.next

	def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
		head = None
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		if l1.val < l2.val:
			head = l1
			l1 = l1.next
		else:
			head = l2
			l2 = l2.next

		head.next = self.mergeTwoLists(l1, l2)
		return head




if __name__ == '__main__':
	n3 = ListNode(4)
	n2 = ListNode(2)
	n1 = ListNode(1)
	n2.next = n3
	n1.next = n2

	l1 = n1

	n4 = ListNode(4)
	n5 = ListNode(3)
	n6 = ListNode(1)
	n6.next = n5
	n5.next = n4
	l2 = n6

	s = Solution()
	res:ListNode = s.mergeTwoLists(l1,l2)
	while res:
		print(res.val)
		res = res.next
