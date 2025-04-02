from tree import *

# Função principal (main) para testes
if __name__ == "__main__":
    arvore = BinaryTree()

    # Inserindo alguns nós
    arvore.inserir_no(5)
    arvore.inserir_no(3)
    arvore.inserir_no(7)
    arvore.inserir_no(2)
    arvore.inserir_no(4)
    arvore.inserir_no(6)
    arvore.inserir_no(8)

    # Exibindo a árvore em pré-ordem
    print("Árvore em pré-ordem:")
    pre_ordem(arvore.root)

