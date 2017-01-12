class Queue:
    def __init__(self):
        self.queues=[]
    def add(self,data):
        self.queues.append(data)
    def remove(self):
        x= self.queues[0]
        y=self.queues[1:]
        self.queues=y
        print x
    def show(self):
        for i in self.queues:
            print "->", i

q=Queue()
q.add(4)
q.add(5)
q.add(6)
q.remove()
q.remove()
q.show()
