#vamos fazer um sistrma de petshop para saber quando o charoro estiver pronto cadastrando cachorro e cliente
class cadastro:
    def __init__(self):
        self.cachorros = []
        self.clientes = []

    def adicionar_cachorro(self):
        nomecachorro = input("Digite o nome do cachorro: ")
        idadecachorro = int(input("Digite a idade do cachorro: "))
        self.cachorros.append((nomecachorro, idadecachorro))

    def adicionar_cliente(self):
        nomecliente = input("Digite o nome do cliente: ")
        idadecliente = int(input("Digite a idade do cliente: "))
        self.clientes.append((nomecliente, idadecliente))

    def acao(self, nomecachorro, idadecachorro):     
        solicitacao = input("tozar ou só banhar?: ")
        if(solicitacao == "tozar"):
            print("cachorro vai ser tozado")
        if(solicitacao == "banhar"):
            print("cachorro vai ser banhado")
            
        print(f"o {nomecachorro}: {solicitacao}, Idade: {idadecachorro}")
        
    def pet(self):
        cachorro = input("cachorro está pronto? (s/n): ")
        while cachorro == "n":
            print("cachorro não está pronto ainda")
            cachorro = input("cachorro está pronto? (s/n): ")
            if cachorro == "s":
                print("cachorro está pronto pode vir buscar")   
                

cadastro = cadastro()
cadastro.adicionar_cachorro()
cadastro.adicionar_cliente()
cadastro.acao(cadastro.cachorros[0][0], cadastro.cachorros[0][1])
cadastro.pet()
