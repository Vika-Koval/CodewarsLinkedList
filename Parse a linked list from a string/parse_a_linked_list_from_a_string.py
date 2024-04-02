def linked_list_from_string(s):
    if s=='None':
        return None
    else:
        s=s.split(' -> ')
        s.pop()
                
        print(s)
        b=int(s[-1])
        node=Node(b,None)
        for i in reversed(s[:-1]):
            i=i.strip()
            node=Node(int(i), node)
        return node
