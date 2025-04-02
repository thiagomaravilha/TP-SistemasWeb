// Função para confirmar exclusão
function confirmarExclusao(event) {
    if (!confirm("Você tem certeza que deseja excluir este item? Esta ação não pode ser desfeita.")) {
        event.preventDefault();
    }
}

// Adicionar o evento de confirmação aos botões de exclusão
document.querySelectorAll('form[action*="excluir"]').forEach(function(form) {
    form.addEventListener('submit', confirmarExclusao);
});
