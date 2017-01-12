class Node:
    def __init__(self,data):
        self.data=data
        self.next_node=None
        self.prev_node=None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new):
        self.next_node=new

    def get_prev(self):
        return self.prev_node

    def set_prev(self,new):
        self.prev_node=new

class double_linked_list:
    def __init__(self):
        self.head=None

    def add_node(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next_node=self.head
            node.prev_node = None
            self.head.prev_node=node
            self.head=node


    def show(self):
        current_node=self.head
        while current_node is not None:

            print current_node.data, "->"
            current_node=current_node.next_node

    def search(self,data):
        current_node=self.head
        index=0
        while current_node is not None:
            if(current_node.data==data):
                print index
            current_node=current_node.next_node
            index=index+1

    def delete(self,data):
        current_node=self.head
        while current_node is not None:
            if(current_node.data==data):
                current_node.prev_node.next_node=current_node.next_node
                current_node.next_node.prev_node=current_node.prev_node
            else:
                current_node=current_node.next_node







s=double_linked_list()
s.add_node('a')
s.add_node('b')
s.add_node('c')

s.add_node('d')
s.add_node('e')
s.show()
s.delete('d')
s.show()
s.search('b')








