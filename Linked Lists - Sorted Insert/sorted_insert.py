""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
def sorted_insert(head, data):
    newItem = data
    if head is None:
        new= Node(newItem)
        new.next=head
        head=new
        return head
    else:
        print(head.data,head.next.data,head.next.next.data)
        probe = head
        if probe.data>data:
            new= Node(data)
            new.next=head
            head=new
            return head
        count=0
        while probe.data<data and probe.next is not None:
            probe = probe.next
            count+=1
            if probe.data<data and probe.next==None:
                count+=1
        probe = head
        while count > 1 :
            probe = probe.next
            count -= 1
        new= Node(newItem)
        new.next=probe.next
        probe.next=new
        return head
