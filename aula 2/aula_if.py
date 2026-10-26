def condicao():
    idade = int(input("Digite sua idade: "))

    if idade:
        if idade >= 14 and idade <= 16:
            print("menor de idade mas já sabe comer sozinho")
            
        if idade >= 16:
            print("já pode votar")
        
        if idade >= 18: 
            print("Você é maior de idade.")
        
    else: 
        print("voce é menor de idade")


def condelif():
        
    numero_1 = float(input("Primeiro número: "))
    numero_2 = float(input("Segundo número: "))

    if numero_1 > numero_2:
        print(f"{numero_1} é o maior número.")
    elif numero_2 > numero_1:
        print(f"{numero_2} é o maior número.")
    elif numero_2 == numero_1:
        print(f"{numero_2} é igual ao {numero_1}.")
    else:
        print("Os números são iguais.")
    
    




