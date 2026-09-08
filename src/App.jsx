import { useEffect, useState } from 'react'

const dinheiro = (valor) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor)

const operacoes = [
  { id: 'sacar', titulo: 'Saque', descricao: 'Retire dinheiro da sua conta', icone: '▥' },
  { id: 'depositar', titulo: 'Depósito', descricao: 'Adicione dinheiro à sua conta', icone: '▤' },
  { id: 'emprestimo', titulo: 'Empréstimo', descricao: 'Simule um novo empréstimo', icone: '◎' },
  { id: 'historico', titulo: 'Extrato', descricao: 'Consulte suas movimentações', icone: '▦' },
]

function App() {
  const [estado, setEstado] = useState({ saldo: 0, transacoes: [] })
  const [operacao, setOperacao] = useState(null)
  const [valor, setValor] = useState('')
  const [parcelas, setParcelas] = useState('3')
  const [mensagem, setMensagem] = useState('')
  const [erro, setErro] = useState('')
  const [carregando, setCarregando] = useState(true)

  const carregarEstado = async () => {
    const resposta = await fetch('/api/estado')
    if (!resposta.ok) throw new Error('Não foi possível conectar à API Python.')
    setEstado(await resposta.json())
  }

  useEffect(() => {
    carregarEstado().catch((problema) => setErro(problema.message)).finally(() => setCarregando(false))
  }, [])

  const selecionarOperacao = (nome) => {
    setMensagem('')
    setErro('')
    setValor('')
    setOperacao(nome)
  }

  const executarOperacao = async (event) => {
    event.preventDefault()
    setMensagem('')
    setErro('')
    const corpo = operacao === 'emprestimo' ? { valor, parcelas } : { valor }
    try {
      const resposta = await fetch(`/api/${operacao}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(corpo) })
      const dados = await resposta.json()
      if (!resposta.ok) throw new Error(dados.erro)
      await carregarEstado()
      setMensagem(dados.mensagem)
      setValor('')
    } catch (problema) {
      setErro(problema.message)
    }
  }

  const voltar = () => { setOperacao(null); setMensagem(''); setErro('') }
  const tituloOperacao = operacoes.find((item) => item.id === operacao)?.titulo

  return (
    <main className="atm-page">
      <header className="atm-header">
        <div className="brand"><span className="brand-symbol">⌁</span><div><strong>CAIXA</strong><small>eletrônico</small></div></div>
      </header>
      <section className="atm-device">
        <div className="screen">
          <div className="screen-heading"><div><p className="kicker">BEM-VINDA, HYRUM</p><h1>{operacao ? tituloOperacao : 'Como podemos ajudar?'}</h1></div><span className="screen-step">{operacao ? '02 / 02' : '01 / 02'}</span></div>
          {!operacao ? <>
            <div className="balance-strip"><div><span>Saldo disponível</span><strong>{carregando ? 'Carregando...' : dinheiro(estado.saldo)}</strong></div><span className="balance-icon">$</span></div>
            <p className="instruction">Selecione uma opção para continuar</p>
            <div className="service-grid">{operacoes.map((item) => <button className="service-option" key={item.id} onClick={() => selecionarOperacao(item.id)}><span className="service-icon">{item.icone}</span><span><strong>{item.titulo}</strong><small>{item.descricao}</small></span><b>›</b></button>)}</div>
          </> : operacao === 'historico' ? <section className="statement"><p className="instruction">Últimas movimentações da conta</p>{estado.transacoes.length === 0 ? <p className="empty-state">Nenhuma transação registrada.</p> : <ul>{estado.transacoes.slice().reverse().map((transacao, indice) => <li key={`${transacao}-${indice}`}><span className="statement-icon">↗</span>{transacao}<b>›</b></li>)}</ul>}</section> : <section className="operation-area"><p className="instruction">Informe os dados da operação</p><form onSubmit={executarOperacao}><label htmlFor="valor">Valor solicitado</label><div className="atm-input"><span>R$</span><input id="valor" type="number" min="0.01" step="0.01" value={valor} onChange={(event) => setValor(event.target.value)} placeholder="0,00" required /></div>{operacao === 'emprestimo' && <><label htmlFor="parcelas">Número de parcelas</label><input id="parcelas" type="number" min="1" value={parcelas} onChange={(event) => setParcelas(event.target.value)} required /></>}<button className="continue-button" type="submit">Continuar <span>›</span></button></form>{mensagem && <p className="feedback success">✓ {mensagem}</p>}{erro && <p className="feedback error">! {erro}</p>}</section>}
          <div className="screen-footer"><button onClick={voltar}>← Voltar</button><span>Não compartilhe sua senha</span><button onClick={() => setOperacao(null)}>Cancelar ×</button></div>
        </div>
        <div className="device-controls"><div className="speaker" /><span>Insira ou aproxime seu cartão</span><div className="card-slot" /></div>
      </section>
      <footer className="atm-footer">Caixa Central <span>•</span> Atendimento disponível todos os dias</footer>
    </main>
  )
}

export default App
