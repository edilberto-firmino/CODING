class cadastro:
    def __init__(self):
        self.veiculos = []
        self.pessoas = []

    def adicionar_veiculo(self):
        nome = input("Digite o nome do veículo: ")
        idade = int(input("Digite a idade do veículo: "))
        self.veiculos.append((nome, idade))

    def adicionar_pessoa(self):
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        self.pessoas.append((nome, idade))

    def exibir_dados(self):     
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        print(f"Nome: {nome}, Idade: {idade}")
