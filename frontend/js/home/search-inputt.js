const inputSearch = document.querySelector('.input-search');

inputSearch.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        const searchQuery = inputSearch.value.trim(); // Captura o valor do input
        if (searchQuery) {
            // Redireciona para outra página, passando o valor como parâmetro
            window.location.href = `/frontend/pesquisar_profi.html?query=${encodeURIComponent(searchQuery)}`;
        }
    }
});
