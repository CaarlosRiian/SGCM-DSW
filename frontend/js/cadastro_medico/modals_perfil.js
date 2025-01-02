const profileBtn = document.getElementById('profile-btn');
const modal = document.getElementById('profile-modal');
const closeModal = document.getElementById('close-modal');
const logoutBtn = document.getElementById('logout-btn');

// Abrir modal ao clicar no botão Meu Perfil
profileBtn.addEventListener('click', (e) => {
    e.preventDefault();
    modal.style.display = 'block';
});

// Fechar modal ao clicar no botão de fechar
closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Fechar modal ao clicar fora do conteúdo
window.addEventListener('click', (e) => {
    // Verificar se o clique foi fora do conteúdo do modal
    if (!e.target.closest('.modal-content') && !e.target.closest('#profile-btn')) {
        modal.style.display = 'none';
    }
});

// Sair (pode adicionar funcionalidades extras aqui)
logoutBtn.addEventListener('click', () => {
    alert('Você saiu!');
    modal.style.display = 'none';
});

