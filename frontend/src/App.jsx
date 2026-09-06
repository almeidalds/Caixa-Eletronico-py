import React, { useState, useEffect } from 'react';
import './index.css';

function App() {
  const [saldo, setSaldo] = useState(0);
  const [mostrarSaldo, setMostrarSaldo] = useState(true);
  const [valorInput, setValorInput] = useState('');
  const [mensagem, setMensagem] = useState('');

  // Busca o saldo direto do Python quando o app abre
  useEffect(() => {
    fetch('http://localhost:8000/api/saldo')
      .then(res => res.json())
      .then(data => setSaldo(data.saldo))
      .catch(err => console.error("Erro ao conectar com o Python:", err));
  }, []);

  const handleSacar = async () => {
    const valor = parseFloat(valorInput);
    if (!valor || valor <= 0) return setMensagem("Digite um valor válido!");

    try {
      const res = await fetch('http://localhost:8000/api/sacar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ valor })
      });
      const data = await res.json();
      
      if (data.erro) {
        setMensagem(data.erro);
      } else {
        setSaldo(data.saldo);
        setMensagem("Saque realizado com sucesso!");
        setValorInput('');
      }
    } catch (error) {
      setMensagem("Erro de comunicação com o servidor.");
    }
  };

  const handleDepositar = async () => {
    const valor = parseFloat(valorInput);
    if (!valor || valor <= 0) return setMensagem("Digite um valor válido!");

    try {
      const res = await fetch('http://localhost:8000/api/depositar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ valor })
      });
      const data = await res.json();
      
      setSaldo(data.saldo);
      setMensagem("Depósito realizado com sucesso!");
      setValorInput('');
    } catch (error) {
      setMensagem("Erro de comunicação com o servidor.");
    }
  };

  return (
    <div className="atm-container">
      <h1>Caixa Eletrônico 🏦</h1>

      <div className="saldo-card">
        <span className="card-label">Saldo Disponível (Python API)</span>
        
        <div className="saldo-valor-container">
          <h2>
            {mostrarSaldo ? `R$ ${saldo.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}` : 'R$ ••••••'}
          </h2>
          <button 
            className="btn-toggle" 
            onClick={() => setMostrarSaldo(!mostrarSaldo)}
          >
            {mostrarSaldo ? '🙈 Ocultar' : '👁️ Mostrar'}
          </button>
        </div>
        
        <span className="card-chip">Conta Corrente • Conectado</span>
      </div>

      <div className="atm-actions">
        <input 
          type="number" 
          placeholder="R$ 0,00" 
          value={valorInput}
          onChange={(e) => setValorInput(e.target.value)}
          className="atm-input"
        />
        
        <div className="btn-group">
          <button onClick={handleSacar} className="btn-action sacar">Sacar</button>
          <button onClick={handleDepositar} className="btn-action depositar">Depositar</button>
        </div>

        {mensagem && <p className="atm-mensagem">{mensagem}</p>}
      </div>
    </div>
  );
} // ou export default App dependendo de como está configurado
export default App;