from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante1 = Restaurante('Ctgafood', 'Fastfood')

bebida_suco = Bebida('Suco de Maracujá', 7.0, 'grande')
prato_macarrao = Prato('Macarrão ao molho', 23.99, 'Macarrão ao molho doce e queijo')


def main():
    print(bebida_suco)
    print(prato_macarrao)

if __name__ == '__main__':
    main()