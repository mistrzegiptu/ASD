class Node:
    def __init__(self, x = None):
        self.next = None
        self.val = x

def nSeries(L):
    res = Node(None)
    tail = res

    if L.next != None:
        return res
    
    val = L.next.val
    
    while L.next != None  and L.next.val >= val:
        tail.next = L
        tail = tail.next
        L.next = L.next.next
        tail.next = None
        val = tail.val

    return res, L

def merge(a, b):
    L = Node(None)
    tail = L

    while a.next != None and b.next != None:
        if a.next.val >= b.next.val:
            tail.next = b.next
            b = b.next
        else:
            tail.next = a.next
            a = a.next
        tail.next = None
        #potencjalnie tail = tail.next

    if a.next != None:
        tail.next = a.next
        a.next = None

    if b.next != None:
        tail.next = b.next
        b = b.next

    while tail.next != None:
        tail = tail.next

    return L, tail

def sort(L):
    while True:
        c = 0
        p = Node(None)
        tail = p

        while L.next != None:
            s1, L = nSeries(L)
            c += 1
            if L.next != None:
                s2, L = nSeries(L)
                c += 1
            else:
                s2 = Node(None)
            m, m_tail = merge(s1, s2)
            tail.next = m.next
            tail = m.tail

        L.next = p.next
        tail = p
        p.next = None

        if c == 1:
            break
    
    return L




head = Node(10)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(3)
head.next.next.next.next = Node(7)
head.next.next.next.next.next = Node(1)

head = sort(head)

while head != None:
    print(head.val)
    head = head.next