// frontend-admin/js/pages/fechamento.js

document.addEventListener("DOMContentLoaded", () => {
    const formAbrir = document.getElementById('formAbrirExpediente');
    const msgAbrir = document.getElementById('msgAbrir');
    const selectVendedor = document.getElementById('vendedorId');

    // 1. Carregar lista de vendedores do Banco de Dados
    async function carregarVendedores() {
        try {
            const response = await fetch('http://localhost:8000/admin/vendedores/');
            const vendedores = await response.json();

            // Limpa o "Carregando..." e coloca a opção padrão
            selectVendedor.innerHTML = '<option value="" disabled selected>Selecione um parceiro na lista...</option>';

            vendedores.forEach(v => {
                // Só mostra na lista quem estiver com status Ativo
                if (v.ativo) {
                    const option = document.createElement('option');
                    option.value = v.id; // O sistema precisa do ID oculto
                    option.textContent = `${v.nome} (PIN: ${v.pin})`; // O usuário vê o Nome e o PIN
                    selectVendedor.appendChild(option);
                }
            });
        } catch (error) {
            selectVendedor.innerHTML = '<option value="" disabled selected>Erro ao carregar parceiros</option>';
            console.error("Erro ao carregar lista de vendedores:", error);
        }
    }

    // Executa a busca assim que entra na tela
    carregarVendedores();

    // 2. Lógica de Envio para Abrir o Expediente
    formAbrir.addEventListener('submit', async (e) => {
        e.preventDefault(); // Impede a página de recarregar

        const vendedorId = selectVendedor.value;

        // Validação de segurança
        if (!vendedorId) {
            msgAbrir.textContent = "Por favor, selecione um parceiro na lista.";
            msgAbrir.className = "text-sm font-bold p-2 rounded text-center bg-red-100 text-red-700 block mb-4";
            return;
        }

        // Monta o "pacote" de dados para enviar ao FastAPI
        const payload = {
            vendedor_id: parseInt(vendedorId),
            litros_pegos: parseFloat(document.getElementById('litrosPegos').value.replace(',', '.')) || 0,
            preco_litro: parseFloat(document.getElementById('precoLitro').value.replace(',', '.')) || 0,
            comissao_fixa: parseFloat(document.getElementById('comissao').value.replace(',', '.')) || 0
        };

        // Altera o botão para mostrar que está processando
        const btnSubmit = formAbrir.querySelector('button[type="submit"]');
        const txtOriginal = btnSubmit.innerHTML;
        btnSubmit.innerHTML = "Iniciando...";
        btnSubmit.disabled = true;

        try {
            // Chamada REAL para o backend
            const response = await fetch('http://localhost:8000/admin/expedientes/abrir', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (!response.ok) throw new Error(data.detail || "Erro ao abrir expediente.");

            // Sucesso!
            msgAbrir.textContent = `Expediente de ${selectVendedor.options[selectVendedor.selectedIndex].text.split('(')[0]} iniciado com sucesso!`;
            msgAbrir.className = "text-sm font-bold p-2 rounded text-center bg-green-100 text-green-700 block mb-4";
            
            // Limpa o formulário para o próximo
            formAbrir.reset();
            selectVendedor.value = ""; 

        } catch (error) {
            // Se der erro (ex: O parceiro já tem um expediente aberto)
            msgAbrir.textContent = error.message;
            msgAbrir.className = "text-sm font-bold p-2 rounded text-center bg-red-100 text-red-700 block mb-4";
        } finally {
            // Restaura o botão
            btnSubmit.innerHTML = txtOriginal;
            btnSubmit.disabled = false;
        }
    });
});