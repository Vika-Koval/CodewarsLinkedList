class Node(object):
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    cursor = Node(None, head)
    seen = set()
    while cursor.next:
        if cursor.next.data in seen:
            temp = cursor.next
            cursor.next = cursor.next.next
            del temp
        else:
            seen.add(cursor.next.data)
            cursor = cursor.next
    return head
