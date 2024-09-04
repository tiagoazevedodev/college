# Tabela: Conjunto de registros.
# Registros: Conjunto de campos que representam um objeto.
# Campos/Chaves: Atributos que representam uma característica do objeto de forma unica
# Uma chave primária é um campo que identifica unicamente um registro.
# Tabela de exemplo:
#
# | ID | Nome | Idade | Sexo |
# |----|------|-------|------|
# | 1  | João | 20    | M    |
# | 2  | Maria| 25    | F    |
#
# Em Python, podemos representar uma tabela como uma lista de dicionários,
# Porém todos os dicionários devem ter as mesmas chaves.

class Table:
    """
    Table implemented by me.
    """
    def __init__(self, maxLenght):
        self.maxLenght = maxLenght
        self.key = [None] * maxLenght
        self.value = [None] * maxLenght
        self.lenght = 0      

    def isEmpty(self):
        return self.key[0] == None
    
    def isFull(self):
        return self.key[self.maxLenght - 1] != None
    
    def getLength(self):
        return self.lenght

    def insert(self, key, value):
        for i in range(self.maxLenght):
            if self.key[i] == None:
                self.key[i] = key
                self.value[i] = value
                return True
        return False
    
    def remove(self, key):
        for i in range(self.maxLenght):
            if self.key[i] == key:
                self.key[i] = None
                self.value[i] = None
                return True
        return False
    
    def search(self, key):
        for i in range(self.maxLenght):
            if self.key[i] == key:
                return self.value[i]
        return None

tabela = Table(10)

carro1 = {
    "Placa": "ABC-1234",
    "marca": "Fiat",
    "modelo": "Uno",
    "ano": 2010
}

carro2 = {
    "Placa": "XYZ-9876",
    "marca": "Chevrolet",
    "modelo": "Celta",
    "ano": 2015
}

carro3 = {
    "Placa": "QWE-4567",
    "marca": "Ford",
    "modelo": "Ka",
    "ano": 2018
}

tabela.insert(carro1["Placa"], carro1)
tabela.insert(carro2["Placa"], carro2)
tabela.insert(carro3["Placa"], carro3)

print(tabela.search(carro1["Placa"]))
print(tabela.search(carro2["Placa"]))

tabela.remove(carro1["Placa"])

print(tabela.search(carro3["Placa"]))

class Tabela:
    """
    Tabela implementada junto com Professor Eduardo.
    """
    def __init__(self, max):
        self.max = max
        self.tamanho = 0
        self.chave = [None] * max
        self.valor = [None] * max

    def inserir(self, chave, valor):
        posicao = self.posicao(chave)
        if posicao != None:
            self.valor[posicao] = valor
            return True
        else:
            if self.tamanho < self.max:
                self.chave[self.tamanho] = chave
                self.valor[self.tamanho] = valor
                self.tamanho += 1
                return True
            else:
                return False

    def buscar(self, chave):
        posicao = 0
        while posicao < self.tamanho:
            if self.chave[posicao] == chave:
                return self.valor[posicao]
            posicao += 1
        return None
    
    def posicao(self, chave):
        posicao = 0
        while posicao < self.tamanho:
            if self.chave[posicao] == chave:
                return posicao
            posicao += 1
        return None
    
    def excluir(self, chave):
        posicao = self.posicao(chave)
        if posicao != None:
            while posicao < self.tamanho - 1:
                self.chave[posicao] = self.chave[posicao + 1]
                self.valor[posicao] = self.valor[posicao + 1]
                posicao += 1

    def printarVetor(self):
        for i in range(self.tamanho):
            print(f"Chave: {self.chave[i]} - Valor: {self.valor[i]}")

    def inserirOrdenado(self, chave, valor):
        if chave != None:
            posicao = self.posicao(chave)
            if posicao != None:
                self.valor[posicao] = valor
                return True
            else:
                if self.tamanho < self.max:
                    controle = self.tamanho
                    while controle > 0 and self.chave[controle - 1] > chave:
                        self.chave[controle] = self.chave[controle - 1]
                        self.valor[controle] = self.valor[controle - 1]
                        controle -= 1
                    self.chave[controle] = chave
                    self.valor[controle] = valor
                    self.tamanho += 1
                    

# tabela = Tabela(10)

# tabela.inserir(1, 10)
# tabela.inserir(2, None)
# tabela.inserir(None, 20)

# print(tabela.printarVetor())
# print(tabela.buscar(None))

class HashTable:
    def __init__(self, max) -> None:
        

    def 