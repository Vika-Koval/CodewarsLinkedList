def loop_size(node):
    fast = node
    slow = node
    flag = False
    count = 0
    while True:
        if not flag:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
        else:
            slow = slow.next
            count += 1
            if slow == fast:
                return count
    return null
