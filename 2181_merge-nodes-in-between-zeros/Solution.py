class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

class Pointer:
    def __init__(self, node: ListNode = None):
        self.node = node

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        p1 = Pointer(head)
        p2 = Pointer(head)
        cumulative_sum = 0

        while p1.node.next is not None:
            p2.node = p2.node.next
            if p2.node.val == 0:
                p2.node.val = cumulative_sum
                cumulative_sum = 0

                p1.node.next = p2.node
                p1.node = p2.node
                
                continue
            cumulative_sum += p2.node.val

        return head.next

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

S = Solution()

l = [0,3,1,0,4,5,2,0]
head = makeLinkedList(l)
printLinkedList(head)

printLinkedList(S.mergeNodes(head))

l = [0,1,0,3,0,2,2,0]
head = makeLinkedList(l)
printLinkedList(head)

printLinkedList(S.mergeNodes(head))