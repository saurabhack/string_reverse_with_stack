class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        return self.head==0
    def push(self,item):
        new_node=node(item)
        if self.head==None:
            self.head=node(item)
            return
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        if self.isempty():
            print('\nstack is already empty')
        top=self.head
        self.head=self.head.next
        top.next=None
        return top.data
    def reverse(self,str):
        size=len(str)
        for i in range(size):
            self.push(str[i])
        str=''
        for i in range(size):
            str+=self.pop()
        return str
if __name__=='__main__':
    s=stack()
    str=str(input("enter your string="))
    print("reversed string=",s.reverse(str))

