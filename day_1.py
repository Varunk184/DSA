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


    def inc_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)



    def insert_value(self,data_list):
        self.head= None
        for i in data_list:
            self.inc_at_end(i)

    def counter(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>self.counter():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head=self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count+=1

    def remove_at(self,index):
        if index<0  or index >=self.counter():
            raise Exception("Invalid index")
        if index==0:
            self.head=self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next

    


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
   # ll.inc_at_beg(54)
    #ll.inc_at_beg(3)
    #ll.inc_at_end(56)
    ll.insert_value(["A","B","C","D"])
    print(ll.counter())

    ll.display()