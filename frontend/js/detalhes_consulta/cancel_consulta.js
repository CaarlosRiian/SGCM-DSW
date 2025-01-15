const cancelButton = document.querySelector('.button-cancel-consutation');
const cancelModal = document.getElementById('cancelConfirmationModal');
const confirmCancelBtn = document.getElementById('confirmCancelBtn');
const closeCancelModalBtn = document.getElementById('closeCancelModalBtn');

const verificationImg = document.querySelector('.verification-1');
const verificationText = document.querySelector('.p-container-details-1');

cancelButton.addEventListener('click', () => {
    cancelModal.style.display = 'flex';
});

closeCancelModalBtn.addEventListener('click', () => {
    cancelModal.style.display = 'none';
});

confirmCancelBtn.addEventListener('click', () => {
    verificationImg.src = "images/detalhes_consulta/cancelada.png";
    verificationText.textContent = "Consulta cancelada"; 
    

    cancelModal.style.display = 'none';
});
 
window.addEventListener('click', (event) => {
    if (event.target === cancelModal) {
        cancelModal.style.display = 'none';
    }
});
