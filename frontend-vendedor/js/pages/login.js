// frontend-vendedor/js/pages/login.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('loginForm');
    const pinInput = document.getElementById('pin');
    const errorMessage = document.getElementById('errorMessage');
    const loginBtn = document.getElementById('loginBtn');

    // Força o PIN a ficar maiúsculo enquanto digita
    pinInput.addEventListener('input', (e) => {
        e.target.value = e.target.value.toUpperCase();
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault(); // Impede a página de recarregar
        
        const pin = pinInput.value.trim();
        if (!pin) return;

        // Estado de "Carregando"
        const btnOriginalText = loginBtn.innerHTML;
        loginBtn.innerHTML = '<span class="animate-pulse">Verificando...</span>';
        loginBtn.disabled = true;
        errorMessage.classList.add('hidden');

        try {
            // Chama a função do arquivo authApi.js
            const dadosVendedor = await loginVendedor(pin);

            // Deu certo! Salva os dados na memória do celular
            localStorage.setItem('sessaoVendedor', JSON.stringify(dadosVendedor));

            // Mostra sucesso
            loginBtn.classList.replace('bg-purple-700', 'bg-green-600');
            loginBtn.innerHTML = '<span>Sucesso!</span>';

            // Vai para a tela principal de venda em 1 segundo
            setTimeout(() => {
                window.location.href = 'app.html';
            }, 1000);

        } catch (error) {
            // Deu errado (PIN falso ou sem expediente aberto)
            errorMessage.textContent = error.message;
            errorMessage.classList.remove('hidden');
            
            // Restaura o botão
            loginBtn.innerHTML = btnOriginalText;
            loginBtn.disabled = false;
            pinInput.value = ''; // Limpa o campo
            pinInput.focus();
        }
    });
});