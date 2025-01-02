const notificationsBtn = document.getElementById('notifications-btn');
const notificationsModal = document.getElementById('notifications-modal');
const closeNotificationsModal = document.getElementById('close-notifications-modal');

// Abrir modal ao clicar no botão de notificações
notificationsBtn.addEventListener('click', (e) => {
    e.preventDefault();
    notificationsModal.style.display = 'block';
});

// Fechar modal ao clicar no botão de fechar
closeNotificationsModal.addEventListener('click', () => {
    notificationsModal.style.display = 'none';
});

// Fechar modal ao clicar fora do conteúdo
window.addEventListener('click', (e) => {
    if (!e.target.closest('.modal-content') && !e.target.closest('#notifications-btn')) {
        notificationsModal.style.display = 'none';
    }
});