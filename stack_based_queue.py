
from asyncio import SafeChildWatcher
from optparse import AmbiguousOptionError
from pickletools import stackslice


class Queue:
    def __init__(self) -> None:
        self.inbound_stack = []
        self.outbound_stack = []

        def enqueue(self, data):
            self.inbound_stack.appen(data)

        def dequeue(self):
            # El principio de las queues basadas en stack
            # consiste en invertir el stack que teníamos 
            # al inicio con pop() poniendo lo que nos saca
            # en otro stack y de esta manera popear los 
            # elementos que entraron de primero en el stack
            # inicial

            # Si outbound está vacío
            if not self.outbound_stack:
                while self.inbound_stack:
                    self.outbound_stack.append(self.inbound_stack.pop())

            return self.outbound_stack.pop()