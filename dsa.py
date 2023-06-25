class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList():
    def __init__(self):
        self.head=None   
    def insertion_at_beg(self,data):
        node=Node(data,self.head)
        self.head=node
        
        
    def print(self):    
        if self.head is None:
            print("List is empyt")
            return
        else:
            itr=self.head
            li=" "
            while itr:
                li+=str(itr.data)+"-->"
                itr=itr.next
            print(li)

if __name__=="__main__":

    ll=LinkedList()
    ll.insertion_at_beg(5)
    ll.insertion_at_beg(4)
    ll.print()