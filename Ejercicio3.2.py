# Ejercicio encontrado en internet el cual Crea una Función 
# para Recorrido en Inorden de un Árbol Binario de Búsqueda

class Nodo:
    def __init__(self, dato):
        self.dato = dato #raiz, el valor del nodo
        self.izquierda = None
        self.derecha = None

def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato, end=" ")
        inorden(raiz.derecha)


raiz = Nodo(21)
insertar(raiz, Nodo (13))
insertar(raiz, Nodo (10))
insertar(raiz, Nodo (33))
insertar(raiz, Nodo (18))
insertar(raiz, Nodo (25))
insertar(raiz, Nodo (40))

# raiz = Nodo('A')
# insertar(raiz, Nodo ('B'))
# insertar(raiz, Nodo ('C'))
# insertar(raiz, Nodo ('D'))
# insertar(raiz, Nodo ('E'))
# insertar(raiz, Nodo ('F'))
# insertar(raiz, Nodo ('G'))

inorden(raiz)

