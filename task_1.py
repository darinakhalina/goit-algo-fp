class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Реверсування однозв'язного списку
    def reverse_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Cортування однозв'язного списку
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            # Немає або тільки один вузол, вже відсортований
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_head

    # Oб'єднує два відсортовані однозв'язні списки в один відсортований список
    def merge_sorted_lists(list1, list2):
        new_list = LinkedList()
        current_list1 = list1.head
        current_list2 = list2.head

        while current_list1 is not None and current_list2 is not None:
            if current_list1.data < current_list2.data:
                new_list.insert_at_end(current_list1.data)
                current_list1 = current_list1.next
            else:
                new_list.insert_at_end(current_list2.data)
                current_list2 = current_list2.next

        while current_list1 is not None:
            new_list.insert_at_end(current_list1.data)
            current_list1 = current_list1.next

        while current_list2 is not None:
            new_list.insert_at_end(current_list2.data)
            current_list2 = current_list2.next

        return new_list


def main():
    list = LinkedList()

    list.insert_at_beginning(1)
    list.insert_at_beginning(2)
    list.insert_at_beginning(3)
    # list.print_list() # 3 2 1

    list.insert_at_end(4)
    list.insert_at_end(5)
    # list.print_list()  # 3 2 1 4 5

    list.insert_at_beginning(6)
    list.insert_at_beginning(7)
    list.insert_at_beginning(8)
    # list.print_list()  # 8 7 6 3 2 1 4 5

    list.reverse_list()
    # list.print_list()  # 5 4 1 2 3 6 7 8

    list.insertion_sort()
    # list.print_list()  # 1 2 3 4 5 6 7 8

    list2 = LinkedList()
    list2.insert_at_beginning(9)
    list2.insert_at_beginning(10)
    list2.insert_at_beginning(11)
    list2.insert_at_end(12)
    list2.insert_at_end(13)
    # list2.print_list()  # 11 10 9 12 13

    list2.insertion_sort()
    # list2.print_list()  # 9 10 11 12 13

    merged_list = LinkedList.merge_sorted_lists(list, list2)
    merged_list.print_list()  # 1 2 3 4 5 6 7 8 9 10 11 12 13


if __name__ == "__main__":
    main()
