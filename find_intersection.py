# This code returns intersection node of two singly-linked lists. It also lets the user to input the data of these two lists. 
# Additionally, it validates the data by removing duplicate values.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def getPreviousNode(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def insertAtEnd(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove(self, node):
        prev_node = self.getPreviousNode(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


def removeDuplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.data
        while current2:
            temp = current2
            current2 = current2.next
            if temp.data == data:
                llist.remove(temp)
        current1 = current1.next

def findIntersection(list1, list2):
    if (list1.head is None or list2.head is None):
        return LinkedList()

    intersection = LinkedList()
    current1 = list1.head
    while current1:
        current2 = list2.head
        data = current1.data
        while current2:
            if current2.data == data:
                node = Node(data)
                intersection.insertAtEnd(node)
                break
            current2 = current2.next
        current1 = current1.next
    removeDuplicates(intersection)

    return intersection


list1 = LinkedList()
list2 = LinkedList()
data_list = input('Enter the elements of the first linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_list1.insertAtEnd(node)
data_list = input('Enter the elements of the second linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_list2.insertAtEnd(node)

intersection = findIntersection(a_list1, a_list2)

print('Their intersection: ')
intersection.display()
