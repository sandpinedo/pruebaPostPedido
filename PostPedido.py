class ArbolPostPedido:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_pedido_traversal(node):
    if node is not None:
        post_pedido_traversal(node.left)# Recorido del sub árbol izquierdo
        post_pedido_traversal(node.right)# Recorido del sub árbol derecho
        print(node.value) # Visitar el nodo actual

# Crear un árbol ejemplo
root = ArbolPostPedido(1)
root.left = ArbolPostPedido(2)
root.right = ArbolPostPedido(3)
root.left.left = ArbolPostPedido(4)
root.left.right = ArbolPostPedido(5)
root.right.left = ArbolPostPedido(6)
root.right.right = ArbolPostPedido(7)

# Realizar el recorrido en post-pedido 
post_pedido_traversal(root)