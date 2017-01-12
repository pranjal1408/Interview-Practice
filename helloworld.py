class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next_node=None

    def getdata(self):
        return self.data

    def getnext_node(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node=new_next

class linked_list():
    def __init__(self):
        self.head=None

    def add_node(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.set_next=self.head
            self.head=node

    def size(self):
        temp=self.head
        size=0
        while(temp):
            temp=temp.getnext_node()
            size=size+1
        return size

    def search_node(self,data):

        temp=self.head
        index =0
        while(temp):
            if(temp.getdata()==data):
                return index
            else:
                temp=temp.getnext_node
            index=index+1

l=linked_list()
l.add_node('a')
l.add_node('b')
print l.size()