class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = "["

        iterator = self.head
        while iterator.next != None:
            result += f" {str(iterator.data)} "
            iterator = iterator.next
        result += f" {str(self.tail.data)} ]"

        return result

    # 접근
    def find_by_index(self, index):
        iterator = self.head
        i = 0
        while i < index:
            iterator = iterator.next
            i += 1

        return iterator.data

    # 탐색
    def find_by_data(self, data):
        iterator = self.head
        find = False
        index = 0
        while iterator.next != None:
            if iterator.data == data:
                find = True
                break
            iterator = iterator.next
            index += 1

        if find == True:
            return index
        else:
            if self.tail.data == data:
                return index
            else:
                return -1

    # 삽입
    # 1. 제일 끝에 삽입
    def append(self, data):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # 2. 제일 앞에 삽입
    def push_front(self, data):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            iterator = self.head
            self.head = new_node
            self.head.next = iterator
        self.size += 1

    # 3. 중간에 삽입
    def push_after(self, index, data):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            iterator = self.head
            i = 0
            while i < index - 1:
                iterator = iterator.next
                i += 1
            new_node.next = iterator.next
            iterator.next = new_node
        self.size += 1

    # 삭제
    # 1. 제일 마지막을 삭제
    def remove(self):
        self.size -= 1
        pass

    # 2. 제일 앞을 삭제
    def delete_font(self):
        self.size -= 1
        pass

    # 3. 중간을 삭제
    def delete_after(self):
        self.size -= 1
        pass


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    pass


class Stack:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def push(self, data):
        self.sll.append(data)

    def pop(self):
        self.sll.remove()

    def peak(self):
        return self.sll.find_by_index(self.sll.size - 1)


class Queue:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def push(self, data):
        pass

    def pop_left(self):
        pass

    def peak(self):
        pass


if __name__ == "__main__":
    # sll = SinglyLinkedList()
    # sll.append(1)
    # sll.append(2)
    # sll.append(3)
    # sll.append(4)
    # print(sll)
    # print(sll.find_by_index(0))
    # print(sll.find_by_index(2))
    # print(sll.find_by_data(-1))

    # dll = DoublyLinkedList()
    # dll.append(1)
    # dll.append(2)
    # dll.append(3)
    # dll.append(4)
    # print(dll)
    # print(dll.find_by_index(0))
    # print(dll.find_by_index(2))
    # print(dll.find_by_data(-1))

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peak())
    stack.pop()
    stack.pop()
    print(stack.peak())