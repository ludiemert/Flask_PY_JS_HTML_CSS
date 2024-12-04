// Variável para controlar o estado do botão
let corDegradadoAtivo = true;

// Função para mudar a cor de fundo ao clicar no botão com degradê em arco-íris
function mudarCor() {
    const botao = document.getElementById("botao-mudar-cor");

    if (corDegradadoAtivo) {
        // Muda o fundo para o degradê arco-íris
        const coresArcoIris = [
            "#ff0000", // Vermelho
            "#ff7f00", // Laranja
            "#ffff00", // Amarelo
            "#00ff00", // Verde
            "#0000ff", // Azul
            "#4b0082", // Anil
            "#9400d3"  // Violeta
        ];

        // Usando o degradê linear para aplicar o efeito de arco-íris no fundo
        document.body.style.background = `linear-gradient(to right, ${coresArcoIris.join(', ')})`;
        document.body.style.backgroundSize = "400% 400%"; // Aumenta a área do gradiente
        document.body.style.animation = "backgroundAnimation 10s ease infinite"; // Anima o fundo

        // Mudar o botão para cor cinza claro
        botao.style.backgroundColor = "#d3d3d3"; // Cor cinza claro
    } else {
        // Se já estiver no estado de cor cinza, volta para o fundo original
        document.body.style.background = "#f4f4f9"; // Cor de fundo original
        botao.style.backgroundColor = "#007bff"; // Cor original do botão
    }

    // Alterna o estado da variável
    corDegradadoAtivo = !corDegradadoAtivo;
}

// Adicionar evento de clique ao botão
document.addEventListener("DOMContentLoaded", () => {
    const botao = document.getElementById("botao-mudar-cor");
    if (botao) {
        botao.addEventListener("click", mudarCor);
    }
});

// Adicionar a animação para o degradê
const styleSheet = document.styleSheets[0];
styleSheet.insertRule(`
    @keyframes backgroundAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
`, styleSheet.cssRules.length);


