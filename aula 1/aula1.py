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

def area():
    comprimento = float(input("Digite o comprimento: "))
    largura = float(input("Digite a largura: "))
    area = comprimento * largura
    print(f"A área é: {area}M²")

def imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc}")

imc()