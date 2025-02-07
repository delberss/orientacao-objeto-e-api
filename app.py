from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

restaurante1 = Restaurante('Ctgafood', 'Fastfood')
restaurante2 = Restaurante('TesteFood', 'Fastfood')

restaurante1.receber_avaliacao('Delber', 10)
restaurante1.receber_avaliacao('Pantera', 8.5)
restaurante1.receber_avaliacao('Maria', 9)
restaurante1.receber_avaliacao('Maria', 7.5)


def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()