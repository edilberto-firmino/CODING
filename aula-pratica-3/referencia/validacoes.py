"""Entrada de dados no terminal, com novas tentativas quando necessário."""

import math


def ler_texto(mensagem):
    """Solicita texto até receber pelo menos um caractere não branco."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("O texto não pode ficar vazio.")


def ler_nota(mensagem):
    """Solicita uma nota finita entre zero e dez; aceita vírgula decimal."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            nota = float(entrada)
        except ValueError:
            print("Digite um número, por exemplo 7.5 ou 7,5.")
            continue
        if not math.isfinite(nota) or not 0 <= nota <= 10:
            print("A nota deve estar entre 0 e 10.")
            continue
        return nota


def ler_opcao():
    """Solicita uma das opções disponíveis no menu."""
    while True:
        opcao = input("Escolha: ").strip()
        if opcao in ("0", "1", "2", "3", "4"):
            return opcao
        print("Opção inválida. Escolha 0, 1, 2, 3 ou 4.")
