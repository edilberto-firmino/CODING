"""Regras da turma, independentes do teclado e da apresentação."""

import math


def calcular_media(notas):
    """Devolve a média ou None quando não há notas.

    Notas devem ser números finitos entre 0 e 10; caso contrário,
    a função sinaliza ValueError. A coleção recebida não é alterada.
    """
    if not notas:
        return None
    for nota in notas:
        if isinstance(nota, bool) or not isinstance(nota, (int, float)):
            raise ValueError("Cada nota deve ser um número entre 0 e 10.")
        if not math.isfinite(nota) or not 0 <= nota <= 10:
            raise ValueError("Cada nota deve ser um número entre 0 e 10.")
    return sum(notas) / len(notas)


def definir_situacao(media):
    """Recebe média válida ou None e devolve a situação acadêmica."""
    if media is None:
        return "Sem notas"
    if media >= 7:
        return "Aprovado"
    if media >= 4:
        return "Recuperação"
    return "Reprovado"


def buscar_aluno(alunos, matricula):
    """Devolve o registro encontrado, ou None quando ausente."""
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def cadastrar_aluno(alunos, matricula, nome, notas):
    """Adiciona um novo registro válido ou sinaliza ValueError.

    Matrícula e nome devem ser strings. Matrícula é única após strip().
    A lista de notas é copiada antes de ser armazenada.
    """
    matricula = matricula.strip()
    nome = nome.strip()
    if not matricula or not nome:
        raise ValueError("Matrícula e nome são obrigatórios.")
    if buscar_aluno(alunos, matricula) is not None:
        raise ValueError("Matrícula já cadastrada.")
    calcular_media(notas)
    aluno = {"matricula": matricula, "nome": nome, "notas": list(notas)}
    alunos.append(aluno)
    return aluno


def resumir_turma(alunos):
    """Conta todos os alunos e calcula a média apenas dos que têm notas."""
    medias = []
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        if media is not None:
            medias.append(media)
    return {
        "total": len(alunos),
        "com_notas": len(medias),
        "media_geral": calcular_media(medias),
    }
