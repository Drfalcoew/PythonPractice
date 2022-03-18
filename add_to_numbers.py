class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        temp_value = ""
        temp_value_b = ""
        temp_node = l1.head
        carried_value = 0
        new_sum = Optional[ListNode]

        while temp_node:
            temp_node = l1.head
            print(temp_node.val)
            temp_value += str(temp_node.val)
            temp_node = l2.head
            temp_value_b += str(temp_node.val)
            temp_node = temp_node.next
        print(temp_value)
        print(temp_value_b)

node2 = ListNode(3)
node1 = ListNode(2, next=node2)
node0 = ListNode(4, next=node1)


node5 = ListNode(1)
node4 = ListNode(0, next=node5)
node3 = ListNode(1, next=node4)

mySolution = Solution().addTwoNumbers()