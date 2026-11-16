from pickle import TRUE


def tuplas1():
    disciplina = ("carlos", "ricardo", "maria", "joao")

    if(disciplina):
        for dis in disciplina:
            print(dis)
    else:   
        print("Disciplina não encontrada")
tuplas1()

def tuplas2():

    turmas_por_periodo = {
        (2026, 1): [
            "Lógica de Programação", 
            "Estruturas de Dados", 
            "Aplicações para Web"],


    }

    periodo = (2026, 1)
    print(turmas_por_periodo[periodo])

tuplas2()
