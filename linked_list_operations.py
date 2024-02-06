
from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def iter(self):
        probe = self.head

        # Recorremos la linked list y entregamos
        # con yield el dato para no guardarlo en
        # la memoria 
        while probe:
            val = probe.data
            probe = probe.next
            yield val

    def element_in_list(self,value):
        for node in self.iter():
            if value == node:
                print(f"{value} is in the linked list")
                return True
        print(f"{value} is not in the list")
        return False

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")
    
    def search_probe(self,target_item):
        probe = self.head
        # Primer encontramos el target_item
        while probe != None and target_item != probe.data:
            probe = probe.next
    
        if probe != None:
            print(f"Target item {target_item} has been found")
        else:
            print(f"Target item {target_item} is not in the linked list")

    def replace_node_value(self, target_item, replace):
        probe = self.head

        # Navegamos la lista hasta encontrar el valor a reemplazar
        while probe != None and target_item != probe.data:
            probe = probe.next

        # reemplazamos
        if probe != None:
            probe.data = replace
            print(f"{replace} replaced the old value in the node with value {target_item}")
        else:
            print(f"The value {target_item} is not int he linked list")

    def insert_value_at_start(self,value):
        self.head = Node(value, self.head)
        self.size += 1

    def append(self, value):
        
        if self.head is None:
            self.insert_value_at_start(value)
        else:
            probe = self.head
            while probe.next != None: # ó while probe.next:
                probe = probe.next
            probe.next = Node(value)

        self.size += 1 

    def delete_node_by_value(self, removed_item):
        
        # Si la lista no tiene elementos
        if self.head is None:
            print("Linked list is empty")

        if self.element_in_list(removed_item):

            # Si la lista tiene 1 elemento
            if self.head.next is None:
                self.head = None
            
            # Si tiene más de 1 elemento
            else:
            # Checkamos si el valor a remover está de primero
                probe = self.head
                if probe.data == removed_item:
                    self.head = probe.next

                else:
                    while probe.next.data != removed_item:
                        probe = probe.next
                    probe.next = probe.next.next
        else:
            print(f"{removed_item} is not in the list")

    def pop(self):

        # Si la lista no tiene elementos
        if self.head is None:
            print("Linked list is empty")
            
            
        else:
            # Si la lista tiene 1 elemento
            if self.head.next is None:
                removed_item = self.head.data
                self.head = None
                print(f"{removed_item} removed")
            
            else:
            # Si tiene más de 1 elemento
                probe = self.head

                while probe.next.next != None:
                    probe = probe.next

                removed_item = probe.next.data
                probe.next = None
                print(f"{removed_item} removed")
        
    def insert_element_by_index(self, index, value):
        # Si es una lista vacía
        if self.head is None or index <= 0:
            self.head = Node(value, self.head)

        else:
            probe = self.head
            # Mientras el indice sea mayor a 1 o probe no sea el último nodo
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1

            probe.next = Node(value,probe.next)

    def delete_node_by_index(self, index):

        ## A este código le faltó la implementación para eliminar el nodo de indice 0
        # # Si es una lista vacía
        # if self.head is None:
        #     print('List was already empty')
        
        # # Si solo hay 1 elemento, vacíe la lista, no matter the index given
        # elif self.head.next is None:
        #     self.head = None
        
        # else:
        #     probe = self.head
        #     while index > 1 and probe.next.next != None:
        #         probe = probe.next

        #     probe.next = probe.next.next

        if index <= 0 or self.head.next is None:
            removed_item = self.head.data
            self.head = self.head.next



                





            

    
    def fill_list(self):
        self.insert_value_at_start('hellow')
        self.insert_value_at_start('buenas')
        self.insert_value_at_start('gudbai')
        self.size +=3


    def print_list(self):

        probe = self.head

        while probe:
            print(probe.data)
            probe = probe.next