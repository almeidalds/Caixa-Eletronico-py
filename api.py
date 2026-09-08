import json
from http.server import BaseHTTPRequestHandler, HTTPServer

import controle
import historico


class CaixaHandler(BaseHTTPRequestHandler):
    def _responder(self, status, dados):
        corpo = json.dumps(dados, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def _ler_corpo(self):
        tamanho = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(tamanho)) if tamanho else {}

    def do_OPTIONS(self):
        self._responder(204, {})

    def do_GET(self):
        if self.path == "/api/estado":
            self._responder(200, {
                "saldo": controle.consultar_saldo(),
                "transacoes": historico.listar_transacoes(),
            })
            return
        self._responder(404, {"erro": "Rota não encontrada."})

    def do_POST(self):
        try:
            dados = self._ler_corpo()
            if self.path == "/api/depositar":
                saldo = controle.depositar(dados["valor"])
                resposta = {"saldo": saldo, "mensagem": "Depósito realizado com sucesso."}
            elif self.path == "/api/sacar":
                saldo = controle.sacar(dados["valor"])
                resposta = {"saldo": saldo, "mensagem": "Saque realizado com sucesso."}
            elif self.path == "/api/emprestimo":
                resposta = controle.simular_emprestimo(dados["valor"], dados["parcelas"])
                resposta["mensagem"] = "Empréstimo aprovado."
            else:
                self._responder(404, {"erro": "Rota não encontrada."})
                return
            self._responder(200, resposta)
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as erro:
            self._responder(400, {"erro": str(erro)})


if __name__ == "__main__":
    print("API do caixa eletrônico em http://localhost:8000")
    HTTPServer(("localhost", 8000), CaixaHandler).serve_forever()