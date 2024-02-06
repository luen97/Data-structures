from node import Node

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self,data):
        node = Node(data)
        
        if self.top: #En caso de que haya algún elemento
             node.next = self.top
             self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        # Si el stack NO está vacío:
        if self.top:
            data = self.top.data
            self.size -= 1

            # Hacemos al top el nodo siguiente
            if self.top.next:
                self.top = self.top.next

            else:
                self.top = None
        
            return data
        
        else:
            return "The stack is empty"

    def peek(self):
        if self.top:
            return self.top
        else:
            return "The stack is empty"

    def clear(self):
        # Así vamos viendo qué vamos sacando
        while self.top:
            self.pop()

        # Así es más rápido
        # self.__init__()
