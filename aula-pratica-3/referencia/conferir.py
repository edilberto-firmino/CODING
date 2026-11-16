"""Conferências de regras e limites. Execute com python conferir.py."""

from turma import (
    buscar_aluno, cadastrar_aluno, calcular_media,
    definir_situacao, resumir_turma,
)


def conferir():
    assert calcular_media([8, 6]) == 7
    assert calcular_media([0, 0]) == 0
    assert calcular_media([10, 10]) == 10
    assert calcular_media([]) is None
    assert definir_situacao(None) == "Sem notas"
    for media, esperado in [(3.9, "Reprovado"), (4, "Recuperação"),
                             (6.9, "Recuperação"), (7, "Aprovado")]:
        assert definir_situacao(media) == esperado

    for notas in [[-1], [11], ["sete"], [float("nan")], [float("inf")], [True]]:
        try:
            calcular_media(notas)
        except ValueError:
            pass  # O erro é o resultado esperado neste caso de teste.
        else:
            raise AssertionError(f"Notas inválidas aceitas: {notas}")

    alunos = []
    assert buscar_aluno(alunos, "999") is None
    assert resumir_turma(alunos) == {"total": 0, "com_notas": 0, "media_geral": None}
    notas = [8, 9]
    cadastrar_aluno(alunos, "001", "Ana", notas)
    notas.append(0)
    assert alunos[0]["notas"] == [8, 9]
    cadastrar_aluno(alunos, "002", "Bruno", [6, 7])
    cadastrar_aluno(alunos, "003", "Carla", [])
    assert buscar_aluno(alunos, "002")["nome"] == "Bruno"
    assert resumir_turma(alunos) == {"total": 3, "com_notas": 2, "media_geral": 7.5}
    assert resumir_turma([alunos[2]])["media_geral"] is None

    for matricula, nome, notas in [(" 001 ", "Outra Ana", [7, 7]),
                                    ("", "Eva", [7, 7]),
                                    ("004", "  ", [7, 7]),
                                    ("004", "Eva", [11, 7])]:
        antes = len(alunos)
        try:
            cadastrar_aluno(alunos, matricula, nome, notas)
        except ValueError:
            assert len(alunos) == antes
        else:
            raise AssertionError("Cadastro inválido foi aceito.")
    print("Conferências concluídas.")


if __name__ == "__main__":
    conferir()
