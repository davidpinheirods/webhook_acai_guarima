// frontend-vendedor/js/api/authApi.js

const BASE_URL = 'http://localhost:8000'; // Endereço do nosso backend no Docker

async function loginVendedor(pin) {
    try {
        const response = await fetch(`${BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ pin: pin })
        });

        const data = await response.json();

        // Se o status da resposta não for 200/201 (Sucesso)
        if (!response.ok) {
            throw new Error(data.detail || "Erro ao fazer login");
        }

        return data; // Retorna os dados (id, nome, expediente_id)
        
    } catch (error) {
        console.error("Erro na API de Login:", error);
        throw error;
    }
}