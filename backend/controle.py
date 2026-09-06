import historico

# 1. Definindo Saldo inicial
saldo = 4261.00

# 2. Loop de repetição princial
while True:
    print("\n--- 🏦 Caixa Eletrônico 🏦 ---")
    print("1. Ver Saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Histórico")
    print("5. Empréstimo")
    print("6. Finalizar")

    # É aqui que o programa vai parar e esperar a pessoa digitar.
    opcao = input("Escolha uma opção: ")
    if opcao == "6":
        print("Saindo do caixa... Até logo!")
        break

    elif opcao == "1":
        print("Seu saldo atual é", saldo)

    elif opcao == "2":
        print("💵 Saque 💵")
        valor_saque = input("Qual o valor deseja sacar? ")
        valor_saque = float(valor_saque) # Atualiza a variável com a versão convertida

        if valor_saque <= saldo: # depois de descobrir o valor do saque
            print("Saca realizado com sucesso")
            saldo = saldo - valor_saque
            historico.registrar_transacao("Saque", valor_saque)
            # Permite o saque: fazemos a subtração do saldo atual.
        else:
            print("Saldo Insuficiente")
        # Bloqueia o saque: Avisamos o cliente que não há dinheiro.

    elif opcao == "3":
        print("💰 Depósito 💰")
        deposito = input("Digite o valor desejado: ")
        deposito =  float(deposito) # Converter valor str() para float()
        saldo = saldo + deposito
        historico.registrar_transacao("Deposito", deposito)

        print("Valor de", deposito, "depositado com sucesso. O Seu saldo atual é de:", saldo)

    elif opcao == "4":
        print("📃 Histórico de Transações 📃")
        for transacao in historico.transacoes:
            print(transacao)

    elif opcao == "5":
        print("💳 Simulação de Empréstimo 💳")
        valor_emprestimo = input("Qual o valor do emprestimo desejado? ")
        valor_emprestimo = float(valor_emprestimo)

        # Solicitar a quantidade de parcelas
        if valor_emprestimo <= saldo *2:
            parcelas = int(input("Em quantas parcelas deseja pagar"))

        # Definindo a taxa de juros com base nas parcelas
            if parcelas <= 3:
                taxa = 0.05 # 5% de juros
            elif parcelas <= 6:
                taxa = 0.10 # 10% de juros
            else:
                taxa = 0.20 # 20% de juros

        # Calcular o valor total das parcelas
            valor_total = valor_emprestimo * (1+ taxa)
            valor_parcela = valor_total / parcelas

            print(f"\n--- Resumo do Empréstimo ---")
            print(f"valor solicitado: R$ {valor_emprestimo:.2f}")
            print(f"Total com juros: {valor_total:.2f}")
            print(f"Parcelando: {parcelas}x de R$ {valor_parcela:.2f}")

            saldo = saldo + valor_emprestimo
            historico.registrar_transacao("Empréstimo", valor_emprestimo)
        else:
             print("Empréstimo negado. O valor excede o limite disponível para o seu saldo.")

    elif opcao == "6":
        print("Saindo do caixa... Até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
