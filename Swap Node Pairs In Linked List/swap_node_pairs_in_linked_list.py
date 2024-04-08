from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    current_node = head
    new_head = head.next
    next = None
    temp = None
    while True:
        next = current_node.next
        temp = next.next
        next.next = current_node
        if temp is None or temp.next is None:
            current_node.next = temp
            break
        current_node.next = temp.next
        current_node = temp
    return new_head
