# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Returns the linked list as a standard python list
    def get_list(self):
        node = self
        l = [node.val]
        while node.next is not None:
            node = node.next
            l.append(node.val)
        return l

class Solution:
    # Traverse the linked list and return the length
    def get_length(self, head: ListNode) -> int:
        n = 1
        while head.next is not None:
            head = head.next
            n += 1
            #print(f"looping {n}")
        return n
    
    # Shortens a list to a given length and returns the new head node
    def shorten_list(self, head: ListNode, length: int) -> ListNode:
        # Traverse the list until we reach the desired length
        print(f"Length: {length}")
        for i in range(length - 1):
            print(f"Node: {head.get_list()}")
            head = head.next

        new_head = head.next # Assign the next node as a new head to be returned
        head.next = None # Set the new node tail to not have a following node

        return new_head

    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        split_list = [] # Split list to return
        if head is None:
            for i in range(k):
                split_list.append(head)
            return split_list
        
        N = self.get_length(head) # Length of the linked list
        size = N // k # The base length of each list
        extra = N % k # The number of lists at the start that have 1 extra items

        print(f"Size: {size}\nExtra: {extra}\n")

        for i in range(k):
            if head is None:
                pass
            elif extra > 0:
                next_head = self.shorten_list(head, size + 1)
                extra -= 1
            else:
                next_head = self.shorten_list(head, size)
            split_list.append(head)
            head = next_head

        return split_list

N10 = ListNode(10)
N9 = ListNode(9, N10)
N8 = ListNode(8, N9)
N7 = ListNode(7, N8)
N6 = ListNode(6, N7)
N5 = ListNode(5, N6)
N4 = ListNode(4, N5)
N3 = ListNode(3, N4)
N2 = ListNode(2, N3)
N1 = ListNode(1, N2)
#N1 = ListNode()

print(f"Input: {N1.get_list()}")

S = Solution()

split_list = S.splitListToParts(N1, 3)

print(f"Split list: {split_list}")

n = 0
for l in split_list:
    if l is None:
        print(f"List {n}: {l}")
    else:
        print(f"List {n}: {l.get_list()}")
    n += 1