class Stack():
    def __init__(self):
        self.stacks=[]

    def push(self,data):
        self.stacks.append(data)

    def pop(self):
        self.stacks.pop()

    def search(self,data):
        y= self.stacks.index(data)
        while y:
            print y

    def show(self):
        for i in self.stacks:
            print "->", i

s=Stack()
s.push('23')
s.push('24')
s.push('abcfdf')
s.pop()
s.push('606')
s.push('pranjal')
s.pop()
s.push('6')
s.push(4)
s.push(55)
s.pop()
s.show()