from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante1 = Restaurante('Ctgafood', 'Fastfood')

bebida_suco = Bebida('Suco de Maracujá', 7.0, 'grande')
bebida_suco2 = Bebida('Suco de Melão', 5.0, 'médio')
bebida_suco3 = Bebida('Suco de Laranja', 10.0, 'grande')

prato_macarrao = Prato('Macarrão ao molho', 23.99, 'Macarrão ao molho doce e queijo')
prato_macarrao2 = Prato('Frango a parmegiana', 23.99, 'Frango a parmegiana')

restaurante1.adicionar_no_cardapio(bebida_suco)
restaurante1.adicionar_no_cardapio(prato_macarrao)
restaurante1.adicionar_no_cardapio(bebida_suco2)
restaurante1.adicionar_no_cardapio(bebida_suco3)
restaurante1.adicionar_no_cardapio(prato_macarrao2)

bebida_suco.aplicar_desconto()


def main():
    restaurante1.exibir_cardapio

if __name__ == '__main__':
    main()