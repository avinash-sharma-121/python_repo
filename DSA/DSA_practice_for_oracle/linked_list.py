class Node:
    def __init__ (self, value):
        self.value=value
        self.next=None


class SinglylinkList:
    def __init__ (self):
        self.head=None

    def insert_at_start(self,value):
        new_node=Node(value)
        if self.head==0:
            self.head=new_node
            return
        
        #temp=self.head
        new_node.next=self.head
        self.head=new_node
    
    def insert_at_end(self,value):
        new_node=Node(value)
        if self.head == None:
            self.head=new_node
            return
        temp=self.head

        while temp.next != None:
            temp=temp.next
        temp.next=new_node

    def print_list(self):
        temp=self.head
        if self.head == None:
            print("no data found")
            return
        while temp != None:
            print(temp.value,end="->")
            temp=temp.next


ll=SinglylinkList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_start(50)
ll.insert_at_start(20)
ll.print_list()
