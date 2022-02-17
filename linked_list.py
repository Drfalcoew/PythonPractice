
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
        self.head_node = Node(value)

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



    def swap_nodes(self, value_a,  value_b):
        print("Swapping Nodes")
        node_a = self.head_node
        node_b = self.head_node
        node_a_prev = None
        node_b_prev = None
        if value_a == value_b:
            print("Swap not necessary. Values are equal")
            return

        while node_a:
            print("In while")
            #  FINDING THE NODES BY THEIR VALUES

            if node_a.get_value() == value_a:
                print(f"Found value a: {node_a.get_value()}")
                break  # If value_a is found, break
            node_a_prev = node_a  # Else, traverse forward, by setting previous node = to current node, and current node = to next node.
            node_a = node_a.get_next_node()

        while node_b:

            if node_b.get_value() == value_b:
                print(f"Found value b: {node_b.get_value()}")
                break  # Same system for finding value_b
            node_b_prev = node_b
            node_b = node_b.get_next_node()



        if node_a is None or node_b is None:  # Swap not possible; One or more values are not found within the list.
            print("Swap not possible")
            return

        # LINKING THE BACK OF THE NODES TO THEIR PREDECESSORS

        if node_a_prev is None:  # If none is before node_a, then node_a must be the head (beginning)
            self.head_node = node_b  # Swapping b for a
        else:
            node_a_prev.set_next_node(node_b)

        if node_b_prev is None:
            self.head_node = node_a
        else:
            node_b_prev.set_next_node(node_a)

        #  LINKING THE FRONT OF THE NODES TO THEIR SUCCESSORS

        temp = node_a.get_next_node
        node_a.set_next_node(node_b.get_next_node())
        node_b.set_next_node(temp)


def main():
    ll = LinkedList(1)

    for i in range(2, 16):
        ll.push_node(i)

    print(ll)

    ll.remove_node(10)
    print(ll)
    print()
    print()
    ll.swap_nodes(15, 9)
    print(ll)



if __name__ == '__main__':
    main()
