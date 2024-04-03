from preloaded import Node
def get_nth(node, index):
    probe = node
    if index<0:
        raise ValueError
    if node is None:
        raise ValueError
    while index > 0:
        probe = probe.next
        print(probe.data)
        index -= 1
    return probe
