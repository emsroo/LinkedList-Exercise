#%%
# Create a Node class to create a Node
class Node:
    def __init__(self, data):
        self.data = data   # guarda la data que me dieron dentro de este vagon
        self.next = None   # el enganche del vagon self.next, su enganche trasero no esta conectado a nada
"""
           +------------------+
           |    mi_nodo       |
           +------------------+
           |                  |
           |  [ BODEGA ]      |  <-- Contiene el dato
           |   data: 10       |
           |                  |
           +------------------+
           |                  |
           |  [ ENGANCHE ]    |  <-- El puntero al siguiente
           |   next: None     |
           |                  |
           +------------------+

"""
# Create a linkedlist class
class LinkedList:
    def __init__(self):  # este es un constructor y se puede acceder a head con self
        self.head = None

    #visualizar la lista completa
    def printLL(self):
        print("Estado actual del tren")
        # Si no hay locomotora, el tren no existe
        if self.head is None:
            print("El tren esta vacio (linkedlist is None)")
            return
        # empezamos con la locomotora y avanzamos
        current_node = self.head
        lista_str = ""
        while current_node:
            lista_str += f" [{current_node.data}] - "
            current_node = current_node.next

        # Anadimos None al final para indicar el final del tren
        lista_str += "None"
        print(lista_str)

    # Method to create a node at the beggining of the LL
    # Create Engage and reasign CABEZA
    def insertAtBegin(self, data):
        # This creates a node with some information that is given as parameter
        new_node = Node(data)
        # Conectamos el enganche del new node para que apunte al mismo lugar que head
        new_node.next = self.head
        # Este es un movimiento clave, cambiamos la cabeza de la lista para que ahora apunte a nuestro nuevo  new_node
        self.head = new_node
        """
         head
             |
             '-----------.
                         |
                         v
                 [ 10 ]  [ 20 ]  [ 30 ] -> None   <-- El antiguo 'head' ya no es el principal
                   ^
                   |
          [ 5 ] ---'
          new_node
        """
    # Method to add a node at any index
    # Indexing starts from zero
    def insertAtIndex(self, data, index):
        # Manejar el caso especial de indice cero
        if index == 0:
            self.insertAtBegin(data) # no need to pass the index, con self se puede acceder
            # a otras funciones de la misma clase
            return

       # Necesito encontrar el nodo que esta justo antes del lugar donde quiero insertar. Empezare en la cabeza head y avanzare vagon por vagon, contando mi posicion, hasta que el siguiente vagon sea la posicion de insercion que busco
       #  Caminas desde la locomotora, pasando por el vagon cero hasta llegar al vagon 1.
       #  una vez que estas en el vagon 1, puedes desacoplarlo del vagon 2 para hacer espacio. Por eso
       #  el bucle termina en el nodo anterior al indice deseado (position + 1 != index)
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
           # debug tool
           print(f"Depurando insert At Index, Posicion: {position} y el indice {index} \n El nodo actual es {current_node.data}")
           position = position + 1
           current_node = current_node.next

        # La insercion: Engachar los vagones
        #    Si encontre el lugar, es decir no me cai del tren, creo mi nuevo nodo. Luego realizo
        #    una operacion de reenganche de dos paso
        if current_node is not None:
            # print(f"El nodo actual es {current_node.data}")
            new_node = Node(data) # creo mi nodo
            new_node.next = current_node.next  # PRIMERO, conecto el enganche de mi nuevo vagon
            # al vagon que estaba despues de mi posicion actual  (current_node). Si no hago esto
            # primero, perdere el resto del tren
            current_node.next = new_node
        #     Segundo, desconecto el current node de su antiguo siguiente y lo engancho
        # El caso fallido, el indice no existe, termino porque current node se convirtio en None
        #     signficia que recorri todo el tren y nunca encontre la posicion deseadada. El indice que me dieron era demasiado grande
        else:
            print("Index not present")
        """
        Estado inicial
          head
           |
           v
         [ 10 ] -> [ 20 ] -> [ 40 ] -> None

        Comienza el bucle while)

        Empieza en current_node = [10], position = 0. ¿0 + 1 != 2? Sí. Avanza.

        Ahora current_node = [20], position = 1. ¿1 + 1 != 2? No, es igual. El bucle se detiene aquí.

        El current_node donde nos detenemos es [20]

        3. LA INSERCIÓN
                   current_node
                        |
                        v
                 ...->[ 20 ] -> [ 40 ] -> None

                      [ 30 ]  <-- new_node

                     current_node
                        |
                        v
                 ...->[ 20 ] -> [ 40 ] -> None
                                ^
                                |
                      [ 30 ] ---'  <-- new_node ahora apunta a [40]   ( new_node.next = current_node.next)

                  current_node
                        |
                        v
                 ...->[ 20 ]    [ 40 ] -> None  <-- Este enlace se rompe  (current_node.next = new_node)
                          \    ^
                           \  /
                            \/
                      [ 30 ] ------'

                  head
                   |
                   v
                 [ 10 ] -> [ 20 ] -> [ 30 ] -> [ 40 ] -> None

        """

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data) # Create new node, that is to create a new wagon, its rear hitch points to nothing
        # Si la lista es None, significa que no hay ningun tren, el nuevo vagon se convierte en el primer y unico de la lista
        # y ahi termina
        if self.head is None:  # no hay ningun tren
            self.head = new_node
            return

        # viajar hasta el ultimo vagon. Si la lista no esta vacia, necesito encontrar el ultimo vagon.
        # Empiezo en la cabeza (head) y avanzo mientras el vagon actual (current_node) tenga un enganche hacia el tro
        current_node = self.head
        while current_node.next: # mientras el vagon en el que estoy este enganchado en otro, paso al siguiente, se va a detener cuando el siguiente sea NONE
            current_node = current_node.next
        # El enganche final, una vez que se ha llegado al ultimo vagon, toma su enganche trasero
        # que apuntaba a NONE y lo conecto a mi new_node
        current_node.next = new_node

        """
         head
           |
           v
         [ 10 ] -> [ 20 ] -> None

                     [ 30 ] -> None   <-- new_node (está listo y esperando)



           current_node (último nodo)   -------> current_node.next = new_node
                |
                v
         ...->[ 20 ]    None  <-- Este enlace se va a modificar
                        /
                       /
              [ 30 ] --'      <-- Se conecta el nuevo nodo
        """
        # update node at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None: # Si encontre el vagon, entonces simplemente accedo
            # a sus datos, y lo reemplazo con el nuevo valor (val)
            current_node.data = val
        else:
            print("Index not present") # si el bucle termino y no encontre nada, entonces, el index no existe
#
        """
                  head
                   |
                   v
                 [ 10 ] -> [ 20 ] -> [ 30 ] -> None

                              current_node
                       |
                       v
 ... -> [ 10 ] -> [ 20 ] -> [ 30 ] -> ...
                  /  |  \
                 /   |   \
                V    V    V
             Cambiando la carga de current_node.data = val

 ... -> [ 10 ] -> [ 25 ] -> [ 30 ] -> ...


        """
    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next


    def remove_last_node(self):
        """
        HEAD
        |
        []
        """
        # Caso 1: si la lista esta vacia, no hay nada que hacer
        if self.head is None:
            return

        # Caso 2: Si el tren solo tiene un vagon
        # Entonces el primer nodo es el ultimo, asi que vaciamos la lista
        """
        [10] -> NONE
        """
        if self.head.next is None:
            self.head = None
            return

        # Caso 3: La lista tiene 2 o mas nodos. Ahora si podemos buscar el punultimo nodo con seguridad
        # Ahora si podemos buscar el penultimo con SEGURIDAD
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        #end while
        current_node.next = None

        # Caso 3:
        """
                        current_node
                             |
                             V
         ... -> [ 10 ] -> [ 20 ]    [ 30 ] -> None  <-- El enlace a [30] se rompe
                             |
                             |  current_node.next
                             '------> None             <-- El nuevo enlace apunta a None
        """

    def removeAtIndex(self, index):
        # Indices negativos
        if index < 0:
            raise IndexError("Negative indices are not supported")

        # Lista vacia
        if self.head is None:
            return

        # Se quiere eliminar el primer nodo (indice 0)
        if index == 0:
            # reutilizamos el metodo que ya funciona para eso
            self.remove_first_node()
            return

        current_node = self.head # comienza con el primer nodo

        """
        Para desenganchar el vagón [C] de un tren [A] -> [B] -> [C] -> [D], no puedes estar parado en [C]. Tienes que estar en el vagón anterior, [B], para poder manipular el enganche que une a [B] con [C].
        """
        position = 0 # empiza un contador
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            # es decir si no esta vacio, y el siguiente tampoco lo esta
            # mueve la referencia del vagon anterior al que tu pusiste el indice y
            # contectalo al siguiente del siguiente
            current_node.next = current_node.next.next
        else:
            # print(f"Index ({index}) not present")
            raise IndexError(f"Index {index} out of range")

    def sizeOfTrain(self):
        size: int = 0
        if self.head is None:
            return 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        print("El tamano del tren es: ",size)
        return size



#   end removeAtIndex






if __name__ == "__main__":

    # creamos nuestro tren
    mi_tren = LinkedList()
    mi_tren.printLL()

    print('\n-- Probando insertAtEnd---')
    mi_tren.insertAtEnd(10)
    mi_tren.insertAtEnd(20)
    mi_tren.insertAtEnd(30)
    mi_tren.insertAtEnd(40)
    mi_tren.printLL()

    print('\n-- Probando insertAtBeggining---')
    mi_tren.insertAtBegin(5)
    mi_tren.printLL()

    print('\n-- Probando insertAtIndex')
    # Insertar en medio
    mi_tren.insertAtIndex(99,2)
    mi_tren.printLL() # esperado: [ 5 ] -> [ 10 ] -> [ 99 ] -> [ 20 ] -> [ 30 ] -> None
    #insertar en un indice que no existe
    mi_tren.insertAtIndex(1000,10)

    print('\n-- Probando updateNode---')
    #actualizar el nodo en la posicion 3 (el 20)
    mi_tren.updateNode(25,3)   # # Esperado: [ 5 ] -> [ 10 ] -> [ 99 ] -> [ 25 ] -> [ 30 ] -> None
    mi_tren.printLL()

    # Actualizar el primer nodo
    mi_tren.updateNode(1,0)
    mi_tren.printLL() #  Esperado: [ 1 ] -> [ 10 ] -> [ 99 ] -> [ 25 ] -> [ 30 ] -> [40] -> None

    # Eliminando un nodo
    print('\n-- Probando Eliminando first Node---')
    mi_tren.remove_first_node()  # self nunca se pasa como parametro
                                 # Esperado   [10] -  [99] -  [25] -  [30] -  [40] - None
    print("El estado de mi tren es: ")
    mi_tren.printLL()

    # Eliminando el nodo del final
    print('\n-- Probando Eliminando Node---')
    mi_tren.remove_last_node()
    mi_tren.printLL()

    # Eliminando en un indice
    mi_tren.removeAtIndex(1)
    mi_tren.printLL()
    mi_tren.removeAtIndex(2)
    mi_tren.printLL()

    # Probando el tamano del tren
    print('\n-- Probando el tamano del tren---')
    mi_tren.sizeOfTrain()


# main


