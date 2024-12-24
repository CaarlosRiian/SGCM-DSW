const fileInput = document.getElementById('customFileInput');
const fileLabel = document.getElementById('customFileLabel');

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        const fileName = fileInput.files[0].name;
        fileLabel.textContent = fileName; 
    } else {
        fileLabel.textContent = 'Escolher arquivo'; 
    }
});

/* Profile pic */

const fileInput_2 = document.getElementById('customFileInput_2');
const fileLabel_2 = document.getElementById('customFileLabel_2');

fileInput_2.addEventListener('change', () => {
    if (fileInput_2.files.length > 0) {
        const fileName = fileInput_2.files[0].name;
        fileLabel_2.textContent = fileName; 
    } else {
        fileLabel.textContent = 'Escolher arquivo'; 
    }
});

