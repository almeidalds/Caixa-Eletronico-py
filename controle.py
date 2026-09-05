import historico

# 1. Definindo Saldo inicial
saldo = 4261.00

# 2. Loop de repetição princial
while True:
    print("\n--- 🏦 Caixa Eletrônico 🏦 ---")
    print("1. Ver Saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Finalizar")
    print("5. Histórico de Transações")

    # É aqui que o programa vai parar e esperar a pessoa digitar.
    opcao = input("Escolha uma opção: ")
    if opcao == "4":
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

    elif opcao == "5":
        print("📃 Histórico de Transações 📃")
        for transacao in historico.transacoes:
            print(transacao)
    
    else:
        print("❌ Opção inválida. Tente novamente.")
