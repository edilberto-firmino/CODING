"""Menu interativo do sistema acadêmico da prática 3."""

from turma import (
    buscar_aluno, cadastrar_aluno, calcular_media,
    definir_situacao, resumir_turma,
)
from validacoes import ler_nota, ler_opcao, ler_texto


def exibir_aluno(aluno):
    """Apresenta um registro, inclusive quando ainda não possui notas."""
    media = calcular_media(aluno["notas"])
    media_exibida = "Sem notas" if media is None else f"{media:.2f}"
    print(f"{aluno['matricula']} | {aluno['nome']} | "
          f"{media_exibida} | {definir_situacao(media)}")


def main():
    """Executa o menu até a escolha de sair; dados ficam na memória."""
    alunos = []
    while True:
        print("\n=== SISTEMA ACADÊMICO ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar matrícula")
        print("4 - Resumir turma")
        print("0 - Sair")
        opcao = ler_opcao()

        if opcao == "0":
            print("Programa encerrado.")
            break
        if opcao == "1":
            matricula = ler_texto("Matrícula: ")
            if buscar_aluno(alunos, matricula) is not None:
                print("Matrícula já cadastrada.")
                continue
            nome = ler_texto("Nome: ")
            notas = [ler_nota("Nota 1: "), ler_nota("Nota 2: ")]
            try:
                cadastrar_aluno(alunos, matricula, nome, notas)
            except ValueError as erro:
                print(f"Cadastro recusado: {erro}")
            else:
                print("Aluno cadastrado.")
        elif opcao == "2":
            if not alunos:
                print("Nenhum aluno cadastrado.")
            for aluno in alunos:
                exibir_aluno(aluno)
        elif opcao == "3":
            matricula = ler_texto("Matrícula a buscar: ")
            aluno = buscar_aluno(alunos, matricula)
            if aluno is None:
                print("Aluno não encontrado.")
            else:
                exibir_aluno(aluno)
        elif opcao == "4":
            resumo = resumir_turma(alunos)
            print(f"Total: {resumo['total']} | Com notas: {resumo['com_notas']}")
            if resumo["media_geral"] is None:
                print("Média geral: Sem dados")
            else:
                print(f"Média geral: {resumo['media_geral']:.2f}")


if __name__ == "__main__":
    main()
