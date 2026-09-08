transacoes = []


def registrar_transacao(tipo, valor):
    transacoes.append(f"{tipo}: R$ {valor:.2f}")


def listar_transacoes():
    return list(transacoes)
