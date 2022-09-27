
class queue2stacks(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def Add(self,item):
        self.stack1.append(item)

    def Remove(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

r= queue2stacks()
r.Add(90)
r.Add(78)
r.Add(40)
r.Add(460)

r.Remove()
r.Remove()
r.Remove()


