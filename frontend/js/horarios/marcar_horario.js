const markAppointmentBtn = document.getElementById('markAppointmentBtn');
const appointmentModal = document.getElementById('appointmentModal');
const confirmBtn = document.getElementById('confirmBtn-marcar-horario');
const cancelBtn = document.getElementById('cancelBtn-marcar-horario');

markAppointmentBtn.addEventListener('click', () => {
    appointmentModal.style.display = 'flex';
});

cancelBtn.addEventListener('click', () => {
    appointmentModal.style.display = 'none';
});

confirmBtn.addEventListener('click', () => {
    appointmentModal.style.display = 'none';
    markAppointmentBtn.textContent = 'Ver Detalhes';
    markAppointmentBtn.addEventListener('click', () => {
        window.location.href = '/frontend/detalhes_consulta.html'; 
    });
});

// Fecha o modal ao clicar fora do conteúdo
window.addEventListener('click', (event) => {
    if (event.target === appointmentModal) {
        appointmentModal.style.display = 'none';
    }
});
