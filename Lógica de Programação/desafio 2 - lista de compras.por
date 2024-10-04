programa {
  funcao inicio() {
    cadeia lista[35]
    inteiro quantidade, contador

    escreva("Quantos itens você deseja comprar? ")
    leia(quantidade)

    para(contador=0;contador<quantidade;contador++){
      escreva("Digite o item ",contador+1," da lista: ")
      leia(lista[contador])
    }

      escreva("Lista de Compras: \n")
      para(contador=0;contador<quantidade;contador++){
        escreva(contador+1," - ", lista[contador],"\n")
      }
  }
}
