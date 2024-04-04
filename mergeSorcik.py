class Node:
    def __init__(self, x = None):
        self.next = None
        self.val = x

def merge(p1, p2):
    head = x = Node()
    head.val = None
    x.val = None
    while p1!=None and p2!=None:
        if p1.val < p2.val:
            head.next = p1
            head = head.next
            p1 = p1.next
        else:
            head.next=p2
            head = head.next
            p2 = p2.next
    if p1 != None:
        head.next = p1
    if p2 != None:
        head.next = p2
    return x.next

#wyciąganie serii naturalnych

def extract(p):
    while p.next != None and p.val <= p.next.val:
        p = p.next
    q = p.next
    p.next = None
    return q

#znajdywanie konca listy

def end(p):
    while p.next != None:
        p = p.next
    return p

def mergesort(p):
    h = Node()
    h.next = p
    e = end(p)
    while True:
        q = extract(p)
        if q == None:
            h.next = p
            return h.next
        z = extract(q)
        x = merge(p,q)
        if z == None:
            h.next = x
            return h.next
        e.next = x
        e = end(x)
        p=z

head = Node(10)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(3)
head.next.next.next.next = Node(7)
head.next.next.next.next.next = Node(1)

head = mergesort(head)

while head != None:
    print(head.val)
    head = head.next