class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DoublyLL:
    def __init__(self,start=None):
        self.start=start
    def isEmpty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.isEmpty():
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next!=None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end='-->')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
                temp.next.prev=None
            else:
                while temp is not None:
                    if temp.item==data:
                        if temp.next is not None:
                            temp.next.prev=temp.prev
                        if temp.prev is not None:
                            temp.prev.next=temp.next
                        else:
                            self.start=temp.next
                        break
                    temp=temp.next
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    
myl=DoublyLL()
myl.insert_at_start(10)
myl.insert_at_last(20)
myl.insert_after(myl.search(10),15)
for x in myl:
    print(x,end=" ")
print()



            
