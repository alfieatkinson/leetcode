# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, head1: ListNode, head2: ListNode) -> ListNode:
        node1 = head1
        node2 = head2

        vals = []

        carry = 0
        while node1 is not None or node2 is not None:
            a = node1.val if node1 else 0
            b = node2.val if node2 else 0

            digit = (a + b + carry) % 10
            carry = (a + b + carry) // 10

            vals.append(digit)

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        
        if carry != 0:
            vals.append(carry)

        print(vals)

        return makeLinkedList(vals)



def makeLinkedList(l: list[int]) -> ListNode:
    l = list(reversed(l))
    node = None
    for i in l:
        node = ListNode(i, node)
    return node

def printLinkedList(root: ListNode) -> ListNode:
    node = root
    while node is not None:
        if node.next is None:
            print(node.val)
        else:
            print(node.val, end=' -> ')
        node = node.next
    print()

l1 = [2,4,3]
l2 = [5,6,4]

head1 = makeLinkedList(l1)
head2 = makeLinkedList(l2)

printLinkedList(head1)
printLinkedList(head2)

S = Solution()

printLinkedList(S.addTwoNumbers(head1, head2))