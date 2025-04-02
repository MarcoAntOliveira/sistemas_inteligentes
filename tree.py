
class No:
    def __init__(self, value, left=None, right=None, up=None, down=None):
        self.pos = value
        self.left_child = left
        self.right_child = right
        self.up_child = up
        self.down_child = down

class BinaryTree:
    def __init__(self):
        self.root = None
        self.next_lis = []
        self.searched = []

    def not_searched(self, pos):
        """Verifica se o valor já foi percorrido"""
        return pos in self.searched

    def inserir_no(self, pos):
        novo = No(pos)
        if self.not_searched(pos):
            print(f"Essa posição {pos} já foi percorrida.")
            return

        self.searched.append(pos)

        if self.root is None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if pos < atual.pos:  # Ir para baixo
                    if atual.down_child is None:
                        anterior.down_child = novo
                        return
                    atual = atual.down_child
                elif pos > atual.pos:  # Ir para cima
                    if atual.up_child is None:
                        anterior.up_child = novo
                        return
                    atual = atual.up_child
                else:
                    # Se o valor for igual, tentamos a direita ou esquerda
                    if atual.right_child is None:
                        anterior.right_child = novo
                        return
                    atual = atual.right_child

# Função para exibir a árvore em pré-ordem
def pre_ordem(no):
    if no:
        print(no.pos, end=" -> ")
        pre_ordem(no.left_child)
        pre_ordem(no.right_child)
        pre_ordem(no.up_child)
        pre_ordem(no.down_child)



    def not_searched(self, pos):
      if pos in self.searched:
        return 1
      return 0
    def retirar_no():
      ...
    def verificar_no():
      ...

