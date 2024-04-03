class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    number=source.data
    source=source.next
    new= Node(number)
    new.next=dest
    dest=new
    return Context(source, dest)
