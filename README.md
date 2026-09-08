# 🏦 Sistema de Caixa Eletrônico (Python)

Este repositório contém um sistema de simulação de Caixa Eletrônico desenvolvido exclusivamente para **práticas pessoais de programação**. O objetivo central deste projeto é exercitar lógica de programação, modularização de código em Python e aprimorar fundamentos de Engenharia de Software (FIAP).

## 📂 O que tem no projeto?

O sistema foi estruturado de forma modular para separar as responsabilidades de controle e registro. Abaixo estão os principais componentes do repositório:

- **`controle.py`**: É o núcleo principal do sistema. Este arquivo gerencia a lógica das operações bancárias, lidando com o fluxo de depósitos, validações de saldo e a execução de saques.
- **`historico.py`**: Módulo responsável pelo armazenamento e estruturação do histórico de transações. É utilizado para registrar cada movimentação (entradas e saídas) e gerar o extrato para o usuário.
- **`LICENSE`**: Arquivo que define os termos de licença e distribuição do código.
- **`.vscode/settings.json`**: Configurações de ambiente do Visual Studio Code para padronizar a formatação e execução do ambiente de desenvolvimento local.

## 🚀 Funcionalidades Esperadas
- **Depósitos**: Adição de valores ao saldo da conta.
- **Saques**: Retirada de valores mediante validação de saldo disponível.
- **Extrato**: Listagem das operações realizadas, utilizando o módulo de histórico.

---
*Desenvolvido por Francisco C. Almeida.*