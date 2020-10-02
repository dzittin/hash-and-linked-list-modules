class _node_:
    def __init__(self, key, value):
        """Nodes of the linked list"""
        self.key = key
        self.value = value
        self.next = None

class linked_list:
    """A object containing a pointer to the head of a linked list"""
    def __init__(self, key, value):
        self.count = 0 # Number of nodes in list
        self.head = None
        self.add_node(key, value)

    def add_node(self, key, value):
        """Nodes with identical keys are allowed"""
        new_node = _node_(key, value)
        self.count += 1
        if self.head == None:
            self.head = new_node
        else:
            prev = self.head
            self.head = new_node
            self.head.next = prev

    def find_value(self, key):
        node = self.find_node(key)
        if node == None:
            return None
        return node.value
    
    def find_node(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return node
            node = node.next
        return None

    def delete_node(self, key):
        """Deletes 1st occurance of Key"""
        """If list is empty or key doesn't exist, return"""
        if self.head == None:
            return
        node = self.head
        while node != None:
            if node.key == key:
                break
            prev = node
            node = node.next
        if node == None:
            return
        elif node == self.head:
            self.head = self.head.next
        else:
            prev.next = node.next
        self.count -= 1
        
    def get_count(self):
        return(self.count)

    def print_list(self):
        if self.head == None:
            return None
        node = self.head
        node_list = []
        while node != None:
            node_list.append((node.key, node.value))
            node = node.next
        return node_list
    
# l1 = linked_list("hi", "there")
# for i in range(1, 10):
#     l1.add_node(i, i + 1)
# lst = l1.print_list()
# #lst.sort()
# print(lst)
# print(l1.get_count())
# l1.delete_node("hi")
# print(l1.get_count())
# print(l1.print_list())