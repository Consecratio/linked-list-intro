class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}'
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        result = []
        temp = self.head

        while temp is not None:
            result.append(temp.data)
            temp = temp.next

        return f'{result}'

    def get_node_at_index(self, index):
        counter = 0
        temp = self.head

        while counter < index:
            if temp.next is None:
                return "out of bounds"
            temp = temp.next
            counter += 1
        
        return temp

    def append(self, new_data):
        temp = self.head
        new_node = Node(new_data)

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def prepend(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node



ll = LinkedList()
n1 = Node(29)
n2 = Node("hello")
n1.next = n2
ll.head = n1

ll.append(1230)

print(ll)