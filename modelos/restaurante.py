from modelos.avaliacao import Avaliacao
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): # init é o construtor | self é para referenciar o objeto
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False # _ deixa o atributo protegido "privado"
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) # quando criar um objeto, ele vai para a propria lista da classe

    def __str__(self): # representação em string de um objeto
        return f'{self._nome} | {self._categoria}'
    
    @classmethod # para indicar que é um METODO DA CLASSE, não de um objeto em si
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'.ljust(20)}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo.ljust(20)}')
        
    @property # modifica como um atributo é lido
    def ativo(self):
        return '✅' if self._ativo else '❌' 
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if nota > 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property # colocando o property ele vira um 'atributo' e não um método ()
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_de_notas = len(self._avaliacao)
            media = round(soma_das_notas / quantidade_de_notas,1)
            return media
        
    def listar_avaliacao(self):
        for index, avaliacao in enumerate(self._avaliacao):
            print(f'[{index+1}]: {avaliacao._cliente}: {avaliacao._nota}')

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): #verifica se o item é uma instancia de ItemCardapio
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        bebidas = []
        pratos = []

        for item in self._cardapio:
            if isinstance(item, Prato):
                pratos.append(item)
            else:
                bebidas.append(item)
        
        print('Bebidas:')
        for i, bebida in enumerate(bebidas, start=1): # começar do item 1
            print(f'{i}. {bebida} | Tamanho: {bebida._tamanho} | Preço: R${bebida._preco:.2f}')

        print('Pratos:')
        for i, prato in enumerate(pratos, start=1):
            print(f'{i}. {prato}')
