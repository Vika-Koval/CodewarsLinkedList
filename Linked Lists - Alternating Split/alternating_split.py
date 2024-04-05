class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    a=[]
    if head is None or head.next is None:
        raise ValueError
    else:
        probe = head
        while probe is not None:
            a.append(probe.data)
            probe = probe.next
    def first(a):
        print(a)
        if len(a)%2==1:
            node1=Node(a[-1])
            for count,i in enumerate(reversed(a[:-1])):
                if count%2==1:
                    new=Node(i)
                    new.next=node1
                    node1=new
            return node1
        else:
            node2=Node(a[-2])
            for count,i in enumerate(reversed(a[:-2])):
                if count%2==1:
                    new=Node(i)
                    new.next=node2
                    node2=new
            return node2
    def second(a):
        if len(a)%2==1:
            node1=Node(a[-2])
            for count,i in enumerate(reversed(a[:-2])):
                if count%2==1:
                    new=Node(i)
                    new.next=node1
                    node1=new
            return node1
        else:
            node2=Node(a[-1])
            for count,i in enumerate(reversed(a[:-1])):
                if count%2==1:
                    new=Node(i)
                    new.next=node2
                    node2=new
            return node2
    return Context(first(a),second(a))
