def stringify(node):
    a=''
    if node is None:
        return 'None'
    else:
        probe = node
        while probe is not None:
            if probe.next is not None:
                a+=f'{probe.data} -> '
            else:
                a+=f'{probe.data} -> None'
            probe = probe.next
    return a
