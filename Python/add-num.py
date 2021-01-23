###
# 14-11-2020
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
###

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, newData):
        newNode = ListNode(newData)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val),
            temp = temp.next


class Solution:
    def insertNumberInLinkedList(self, n):
        nLinkList = LinkedList()
        for i in [int(i) for i in str(n)]:
            nLinkList.append(i)

        return nLinkList

    def extractNumberFromLinkedList(self, linklist):
        number = linklist.val
        extractLinkList = linklist.next
        while extractLinkList:
            number = int(str(number) + str(extractLinkList.val))
            extractLinkList = extractLinkList.next
        return number

    def reverseInt(self, n):
        reversed = 0

        while(n != 0):
            r = int(n % 10)
            reversed = reversed*10 + r
            n = int(n/10)

        return reversed

    def addTwoNumbers(self, l1, l2, c=0):
        n1 = self.reverseInt(self.extractNumberFromLinkedList(l1))
        n2 = self.reverseInt(self.extractNumberFromLinkedList(l2))
        numberSum = n1 + n2

        return self.insertNumberInLinkedList(numberSum)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

result.printList()
