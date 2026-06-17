// frontend-vendedor/js/pages/app.js

document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Verificação de Segurança
    const sessaoStr = localStorage.getItem('sessaoVendedor');
    if (!sessaoStr) {
        window.location.href = 'index.html';
        return;
    }

    const sessao = JSON.parse(sessaoStr);

    // 2. Preenche o nome do usuário
    document.getElementById('nomeVendedor').textContent = sessao.nome;
    
    // 3. Busca os dados reais no banco
    async function carregarStatus() {
        try {
            const response = await fetch(`http://localhost:8000/vendedor/app/status/${sessao.expediente_id}`);
            
            if (!response.ok) {
                throw new Error(`Erro do servidor: ${response.status}`);
            }
            
            const dados = await response.json();

            const formatarMoeda = (valor) => valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

            document.getElementById('statPegos').textContent = `${dados.litros_pegos.toFixed(1)} L`.replace('.', ',');
            
            document.getElementById('statVendidos').parentElement.querySelector('span').textContent = "TOTAL PIX";
            document.getElementById('statVendidos').textContent = formatarMoeda(dados.total_pix);
            
            document.getElementById('statComissao').parentElement.querySelector('span').textContent = "COMISSÃO PIX";
            document.getElementById('statComissao').textContent = formatarMoeda(dados.comissao_pix);

        } catch (error) {
            console.error("Erro ao carregar status:", error);
        }
    }

    carregarStatus();

    // 4. Lógica de Logout
    document.getElementById('btnLogout').addEventListener('click', () => {
        localStorage.removeItem('sessaoVendedor');
        window.location.href = 'index.html';
    });

    // 5. Gerar os botões de 0.5L até 10L dinamicamente
    const grid = document.getElementById('gridLitros');
    
    for (let litros = 0.5; litros <= 10; litros += 0.5) {
        const btn = document.createElement('button');
        
        btn.className = "bg-white border-2 border-purple-200 text-purple-700 font-black text-2xl py-6 rounded-2xl shadow-sm active:bg-purple-700 active:text-white transition-colors";
        
        const textoLitro = litros.toFixed(1).replace('.', ',');
        btn.textContent = `${textoLitro} L`;
        
        btn.onclick = () => abrirModalPix(textoLitro, litros, sessao);
        
        grid.appendChild(btn);
    }

    // 6. Lógica do Modal
    const modal = document.getElementById('modalPix');
    const btnFechar = document.getElementById('btnFecharModal');

    btnFechar.addEventListener('click', () => {
        modal.classList.add('hidden');
    });

});

// Função chamada ao clicar em qualquer botão de litro
function abrirModalPix(textoLitro, litrosNumero, sessao) {
    const modal = document.getElementById('modalPix');
    const textoQuantidade = document.getElementById('modalQuantidade');

    textoQuantidade.textContent = `${textoLitro} Litros`;
    modal.classList.remove('hidden');
}