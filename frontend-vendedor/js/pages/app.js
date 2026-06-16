// frontend-vendedor/js/pages/app.js

document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Verificação de Segurança (Protege a rota)
    const sessaoStr = localStorage.getItem('sessaoVendedor');
    if (!sessaoStr) {
        // Se não tiver sessão salva, joga de volta pro login
        window.location.href = 'index.html';
        return;
    }

    const sessao = JSON.parse(sessaoStr);

    // 2. Preenche os dados do usuário e do Dashboard no cabeçalho
    document.getElementById('nomeVendedor').textContent = sessao.nome;

    // 3. Lógica de Logout
    document.getElementById('btnLogout').addEventListener('click', () => {
        localStorage.removeItem('sessaoVendedor');
        window.location.href = 'index.html';
    });

    // 4. Gerar os botões de 0.5L até 10L dinamicamente
    const grid = document.getElementById('gridLitros');
    
    for (let litros = 0.5; litros <= 10; litros += 0.5) {
        const btn = document.createElement('button');
        
        // Estilização do botão (Tailwind)
        btn.className = "bg-white border-2 border-purple-200 text-purple-700 font-black text-2xl py-6 rounded-2xl shadow-sm active:bg-purple-700 active:text-white transition-colors";
        
        // Formata o número (Ex: 1.5 vira "1,5 L")
        const textoLitro = litros.toFixed(1).replace('.', ',');
        btn.textContent = `${textoLitro} L`;
        
        // Adiciona o evento de clique para abrir o Modal
        btn.onclick = () => abrirModalPix(textoLitro, litros, sessao);
        
        grid.appendChild(btn);
    }

    // 5. Lógica do Modal
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

    // Atualiza o texto do modal com a quantidade clicada
    textoQuantidade.textContent = `${textoLitro} Litros`;
    
    // Mostra o modal na tela
    modal.classList.remove('hidden');

    /* AQUI ENTRARÁ A INTEGRAÇÃO COM O BACKEND:
       1. Pegaremos o 'sessao.expediente_id' e o 'litrosNumero'
       2. Enviaremos via POST para a nossa futura API do Pix
       3. O backend calculará (Litros * Preço do Dia) e retornará o QR Code
    */
}