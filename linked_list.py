from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        # Si no hay nodos, agregar el creado a la cola
        if self.tail == None:
            self.tail = node
        else:

        # Le digo a current que se ubique en el nodo tail
        # que es el primer nodo, luego le digo que itere 
        # mientras current.next sea distinto de None, es
        # decir, al final de la lista. Cuando llegue ahí, 
        # asignele a ese último nodo el nodo recién creado 
        # en su atributo next, así es como queda linkeado
            current = self.tail

        # Mientras current.next apunte a algún lugar o
        # su retorno NO sea false, ejecute la iteración
            while current.next:
                current = current.next

            current.next = node
        
        self.size += 1

        def size(self):
            return str(self.size)

    def iter(self):
        current = self.tail

        # Recorremos la linked list y entregamos
        # con yield el dato para no guardarlo en
        # la memoria 
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):

        # Hacemos a current y previous ser los 
        # primeros nodos de la lista
        current = self.tail
        previous = self.tail

        while current:
            if current == data:
                # Si el vigente es el dato que buscamos
                # y este es igual al primer nodo,
                # reasignamos el primer nodo al siguiente
                # es decir el segundo
                if current == self.tail:
                    self.tail = current.next

                else:

                # De lo contrario, hacemos que la referencia
                # del siguiente nodo de previous sea el si-
                # guiente nodo de current: No borramos el nodo
                # sino que quitamos el link que tenía con su
                # nodo anterior y se lo ponemos al nodo siguiente
                    previous.next = current.next
                    self.size -= 1
                    return current.data

            
            # No hemos encontrado el dato, seguir buscando
            # recorriendo la lista
            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

    def replace_node_value(self, value, replace):
        probe = self.tail

        # Navegamos la lista hasta encontrar el valor a reemplazar
        while probe != None and value != probe.data:
            probe = probe.next

        # reemplazamos
        if probe != None:
            probe.data = replace
            print(f"{replace} replaced the old value in the node with value {value}")
        else:
            print(f"The value {value} is not int he linked list")

    def print_list(self):

        current = self.tail

        while current:
            print(current.data)
            current = current.next





if __name__ == "__main__":
    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('spam')

    current = words.tail

    while current:
        print(current.data)
        current = current.next

    for word in words.iter():
        print(word)

    words.search('spam')
    words.search('arepa') #No imprime nada

    words.replace_node_value('spam', 'calabaza')

    words.print_list()