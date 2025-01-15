const openModalBtn = document.getElementById('openModalBtn');
const closeModalBtn = document.getElementById('closeModalBtn');
const modal = document.getElementById('passwordModal');
const inputs = modal.querySelectorAll('input'); 

openModalBtn.addEventListener('click', () => {
  modal.style.display = 'flex';
});

closeModalBtn.addEventListener('click', () => {
  modal.style.display = 'none';
  clearInputs(); 
});

window.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.style.display = 'none';
    clearInputs();
  }
});

function clearInputs() {
  inputs.forEach((input) => {
    input.value = '';
  });
}

window.addEventListener('click', (event) => {
  if (event.target === cancelModal) {
      cancelModal.style.display = 'none';
  }
});

