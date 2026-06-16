// frontend-admin/js/pages/parceiros.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('formVendedor');
    const msg = document.getElementById('msgVendedor');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const nome = document.getElementById('nomeVendedor').value;
        const pin = document.getElementById('pinVendedor').value.toUpperCase();

        try {
            // Chamada REAL para o nosso backend
            const response = await fetch('http://localhost:8000/admin/vendedores/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ nome: nome, pin: pin })
            });

            const data = await response.json();

            if (!response.ok) throw new Error(data.detail || "Erro ao cadastrar.");

            // Sucesso
            msg.textContent = "Vendedor cadastrado com sucesso!";
            msg.className = "text-sm font-bold p-2 rounded text-center bg-green-100 text-green-700 block";
            form.reset(); // Limpa o formulário

        } catch (error) {
            // Erro (ex: PIN já existe)
            msg.textContent = error.message;
            msg.className = "text-sm font-bold p-2 rounded text-center bg-red-100 text-red-700 block";
        }
    });

// Função para carregar os dados reais do banco
    async function carregarVendedores() {
        const tbody = document.getElementById('tabelaVendedores');
        tbody.innerHTML = '<tr><td colspan="4" class="py-4 text-center text-gray-500">Carregando...</td></tr>';

        try {
            const response = await fetch('http://localhost:8000/admin/vendedores/');
            const vendedores = await response.json();

            tbody.innerHTML = ''; // Limpa o "Carregando"

            if (vendedores.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" class="py-4 text-center text-gray-500">Nenhum vendedor cadastrado.</td></tr>';
                return;
            }

            vendedores.forEach(v => {
                // Traduz o booleano 'ativo' para um visual bonito
                const statusHtml = v.ativo 
                    ? `<span class="bg-green-100 text-green-700 px-2 py-1 rounded text-xs font-bold uppercase">Ativo</span>`
                    : `<span class="bg-red-100 text-red-700 px-2 py-1 rounded text-xs font-bold uppercase">Inativo</span>`;

                tbody.innerHTML += `
                    <tr class="border-b hover:bg-gray-50">
                        <td class="py-3 px-4 text-gray-500">#${v.id}</td>
                        <td class="py-3 px-4 font-bold">${v.nome}</td>
                        <td class="py-3 px-4 font-mono">${v.pin}</td>
                        <td class="py-3 px-4">${statusHtml}</td>
                    </tr>
                `;
            });
        } catch (error) {
            tbody.innerHTML = '<tr><td colspan="4" class="py-4 text-center text-red-500 font-bold">Erro ao carregar dados.</td></tr>';
        }
    }

    // Chama a função assim que a página carregar
    carregarVendedores();

});