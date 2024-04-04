class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
def reverse(head):
    a=[]
    if head is None:
        return None
    while head!= None:
        removedItem = head.data
        if head.next is None:
            head = None 
        else:
            probe = head
            while probe.next.next is not None:
                probe = probe.next
            removedItem = probe.next.data
            probe.next = None
        a.append(removedItem)
        print('removed',removedItem,a)
    b=int(a[-1])
    node=Node(b)
    for i in reversed(a[:-1]):
        new=Node(int(i))
        new.next=node
        node=new
    return node
    
