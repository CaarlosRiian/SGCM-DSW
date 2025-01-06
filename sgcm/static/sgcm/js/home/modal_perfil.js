const profileBtn = document.getElementById('profile-btn');
const modal = document.getElementById('profile-modal');
const closeModal = document.getElementById('close-modal');
const logoutBtn = document.getElementById('logout-btn');

profileBtn.addEventListener('click', (e) => {
    e.preventDefault();
    modal.style.display = 'block';
});

closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
});

window.addEventListener('click', (e) => {
    if (!e.target.closest('.modal-content') && !e.target.closest('#profile-btn')) {
        modal.style.display = 'none';
    }
});

logoutBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

