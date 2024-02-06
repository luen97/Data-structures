class TwoWayNode():
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        # Creamos el nodo previo a agregarlo
        new_node = TwoWayNode(data, None, None)

        # Si el queue está vacío
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            # El anterior al nuevo nodo sería la cola
            # _ _ _ tail new_node
            new_node.previous = self.tail
            # Y el que va después de la cola es el
            # nuevo nodo
            self.tail.next = new_node
            # finalmente actualizamos la cola
            self.tail = new_node
        
        self.count += 1
    
    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None

        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data