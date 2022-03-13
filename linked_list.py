
#  Linked List

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        if type(next_node) == Node:
            self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = None if value == None else Node(value)

    def __repr__(self):  # Returns a string representation of the list
        stringified_list = ""
        node = self.head_node
        while node:
            stringified_list += str(node.value) + " "
            node = node.get_next_node()
        return stringified_list

    def push_node(self, value):  # Add node to head of list
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def pop_node(self):  # LIFO (Last In, First Out)
        pass

    def remove_node(self, value):  # remove specific value
        current_node = self.head_node
        value_to_remove = value
        if self.head_node.get_value() is value_to_remove:
            self.head_node = self.head_node.get_next_node()
        else:
            while current_node:  # while
                if current_node.get_next_node().get_value() == value_to_remove:
                    current_node.set_next_node(current_node.get_next_node().next_node)
                    current_node = None  # exits loop
                else:
                    current_node = current_node.get_next_node()


    def length(self):
        total = 0
        temp_node = self.head_node
        while temp_node:
            temp_node = temp_node.get_next_node()
            total+=1
        return total

    def get_at_index(self, index):
        if self.length() <= index < 0:
            return None


        temp_node = self.head_node
        temp_index = 0
        while temp_node:
            print('passed index: {}, temp index: {}'.format(index, temp_index))
            if index == temp_index:
                return temp_node.get_value()
            temp_node = temp_node.get_next_node()
            temp_index+=1




    def swap_nodes(self, x,  y):
        if x == y:
            return

            # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head_node
        while currX != None and currX.value != x:
            prevX = currX
            currX = currX.next_node

        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head_node
        while currY != None and currY.value != y:
            prevY = currY
            currY = currY.next_node

        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next_node = currY
        else:  # make y the new head
            self.head_node = currY

        # If y is not head of linked list
        if prevY != None:
            prevY.next_node = currX
        else:  # make x the new head
            self.head_node = currX

        # Swap next pointers
        temp = currX.next_node
        currX.next_node = currY.next_node
        currY.next_node = temp


def main():
    ll = LinkedList()
    for i in range(10, 0, -1):
        print(i)
        ll.push_node(i)

    print(ll)

    ll.remove_node(8)
    print()
    print()
    ll.swap_nodes(4, 5)
    print(ll)
    x = input("Get value at index: ")
    print("\n\nMy value at index {} = {}".format(x, ll.get_at_index(int(x))))



if __name__ == '__main__':
    main()
