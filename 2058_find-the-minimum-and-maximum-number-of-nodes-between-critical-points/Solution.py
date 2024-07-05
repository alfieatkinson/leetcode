# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        # Initialize variables to store the positions of critical points
        critical_points = []
        index = 0
        prev = None
        current = head
        
        # Traverse the list to identify critical points
        while current and current.next:
            if prev is not None and current.next is not None:
                if (current.val > prev.val and current.val > current.next.val) or (current.val < prev.val and current.val < current.next.val):
                    critical_points.append(index)
            prev = current
            current = current.next
            index += 1

        # If there are fewer than two critical points, return [-1, -1]
        if len(critical_points) < 2:
            return [-1, -1]
        
        # Calculate the minimum and maximum distances
        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]
        
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        
        return [min_distance, max_distance]

# Example usage:
# list = [5, 3, 1, 2, 5, 1, 2]
# Construct the linked list
nodes = [ListNode(5), ListNode(3), ListNode(1), ListNode(2), ListNode(5), ListNode(1), ListNode(2)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
head = nodes[0]

sol = Solution()
print(sol.nodesBetweenCriticalPoints(head))  # Output: [1, 3]