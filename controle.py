import historico

# Saldo inicial de exemplo. Em um sistema real, isso seria armazenado em um banco de dados.
saldo = 4261.00


def consultar_saldo():
    return saldo


def sacar(valor):
    global saldo
    valor = float(valor)
    if valor <= 0:
        raise ValueError("O valor do saque deve ser maior que zero.")
    if valor > saldo:
        raise ValueError("Saldo insuficiente.")
    saldo -= valor
    historico.registrar_transacao("Saque", valor)
    return saldo


def depositar(valor):
    global saldo
    valor = float(valor)
    if valor <= 0:
        raise ValueError("O valor do depósito deve ser maior que zero.")
    saldo += valor
    historico.registrar_transacao("Depósito", valor)
    return saldo


def simular_emprestimo(valor, parcelas):
    global saldo
    valor = float(valor)
    parcelas = int(parcelas)
    if valor <= 0 or parcelas <= 0:
        raise ValueError("Informe valores positivos para o empréstimo.")
    if valor > saldo * 2:
        raise ValueError("O valor excede o limite disponível para o seu saldo.")

    taxa = 0.05 if parcelas <= 3 else 0.10 if parcelas <= 6 else 0.20
    valor_total = valor * (1 + taxa)
    saldo += valor
    historico.registrar_transacao("Empréstimo", valor)
    return {
        "valor": valor,
        "parcelas": parcelas,
        "taxa": taxa,
        "valor_total": valor_total,
        "valor_parcela": valor_total / parcelas,
        "saldo": saldo,
    }


if __name__ == "__main__":
    print("Use api.py para iniciar a interface web do caixa eletrônico.")
