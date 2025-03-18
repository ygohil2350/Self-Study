# Add Two Numbers
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         newNode = ListNode(data)
#         if self.head is None:
#             self.head = newNode
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = newNode

#     def print(self):
#         current = self.head
#         while current:
#             print(current.val, end=" -> ")
#             current = current.next
#         print("None")


# def createLinkListFromArray(inputArr):
#     link_list = LinkedList()
#     for currentInput in inputArr:
#         link_list.append(currentInput)
#     return link_list


# inputArr1 = [2, 4, 3]
# inputArr2 = [5, 6, 4]

# l1 = createLinkListFromArray(inputArr1)
# l2 = createLinkListFromArray(inputArr2)


# def addTwoNumbers(l1, l2):
#     sumArray = LinkedList()
#     head1 = l1.head
#     head2 = l2.head
#     extra = 0
#     while head1 or head2 or extra:
#         sumOfTwoDigit = extra
#         if head1.val:
#             sumOfTwoDigit += head1.val
#         if head1.val:
#             sumOfTwoDigit += head2.val
#         if sumOfTwoDigit < 10:
#             sumArray.append(sumOfTwoDigit)
#             extra = 0
#         else:
#             sumArray.append(sumOfTwoDigit % 10)
#             extra = sumOfTwoDigit // 10
#         if head1:
#             head1 = head1.next
#         if head2:
#             head2 = head2.next
#     sumArray.print()


# addTwoNumbers(l1, l2)
