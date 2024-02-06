

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


if __name__ == "__main__":
    node1 = None
    node2 = Node("A",None)
    node3 = Node("B",node2)

    head = None
    for count in range(1,5):
        head = Node(count, head)

    while head != None:
        print(head.data)
        head = head.next

    
    i = 0
    l = [True,True,True,None,True]

    while l[i]:
        i += 1
        print(l[i])