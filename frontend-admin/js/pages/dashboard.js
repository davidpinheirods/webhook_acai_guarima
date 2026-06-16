// frontend-admin/js/pages/dashboard.js

document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Coloca a data de hoje no topo
    const dataDisplay = document.getElementById('dataAtual');
    const hoje = new Date();
    dataDisplay.textContent = hoje.toLocaleDateString('pt-BR', {
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric'
    });

async function carregarDashboard() {
        try {
            const response = await fetch('http://localhost:8000/admin/dashboard/resumo');
            const dados = await response.json();

            // Preenche os cartões
            document.getElementById('dashAcessoRua').textContent = dados.litros_na_rua.toFixed(1).replace('.', ',');
            document.getElementById('dashPix').textContent = dados.pix_recebidos.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
            document.getElementById('dashParceiros').textContent = dados.parceiros_ativos;

            // Preenche a tabela
            const tbody = document.getElementById('tabelaExpedientes');
            tbody.innerHTML = '';

            if (dados.expedientes.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" class="py-4 text-center text-gray-500">Nenhum expediente aberto hoje.</td></tr>';
                return;
            }

            dados.expedientes.forEach(exp => {
                const tr = document.createElement('tr');
                tr.className = "border-b hover:bg-gray-50 transition-colors";
                
                tr.innerHTML = `
                    <td class="py-4 px-4 font-bold">${exp.nome}</td>
                    <td class="py-4 px-4">${exp.pegos.toFixed(1).replace('.', ',')} L</td>
                    <td class="py-4 px-4">R$ ${exp.preco.toFixed(2).replace('.', ',')}</td>
                    <td class="py-4 px-4">
                        <span class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-xs font-bold uppercase animate-pulse">
                            ${exp.status}
                        </span>
                    </td>
                `;
                tbody.appendChild(tr);
            });

        } catch (error) {
            console.error("Erro ao carregar dashboard:", error);
        }
    }

    carregarDashboard();

});