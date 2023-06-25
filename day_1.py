class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None
    def inc_at_beg(self,data):
        node = Node(data,self.head)
        self.head=node
    def display(self):
        itr = self.head
        li=" "
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            while itr:
                li += str(itr.data)+"--->"
                itr = itr.next
            print(li)

if __name__=="__main__":
    ll = Linkedlist()
    ll.inc_at_beg(54)
    ll.inc_at_beg(3)
    ll.display()