class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def insert(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return

        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
    
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        result = "["
        current = self.head
        while current:
            result += str(current.data)
            if current.next:
                result += " -> "
            current = current.next
        result += "]"
        return result
    
    def get_value_by_index(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None




my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(45)
my_list.append(66)
my_list.append(1001)
my_list.append(2034.22)
my_list.print_list()





# 1-ое задание
size = my_list.size()
print(size)
# 2-ое задание
print(my_list)
# 3-ье задание
value = my_list.get_value_by_index(5)
print(value)