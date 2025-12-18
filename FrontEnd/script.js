
const API = "http://127.0.0.1:8000";
const attBtn = document.getElementById("attBtn")
async function carregarGols() {
    try {
        const response = await fetch(`${API}/Gols`);
        if (!response.ok) throw new Error(`Erro na requisição: ${response.status}`);

        const gols = await response.json();
        exibirGols(gols.response);

    } catch (error) {
        console.error("Não foi possível carregar os dados:", error);
        document.getElementById('Feed').innerHTML = '<p>Erro ao carregar dados.</p>';
    }
}

function exibirGols(listaDeGols) {
    const container = document.getElementById('Feed');
    container.innerHTML = "";

    listaDeGols.forEach(gol => {
        const postDiv = document.createElement('div');
        postDiv.classList.add('post-item');

        const dataFormatada = new Date(gol.date).toLocaleDateString('pt-BR');
        const times = gol.title.split("-")
        const competicao = gol.competition.split(":")
        const video = gol.videos[0]?.embed.split("'")
        postDiv.innerHTML = `
            <h2>${times[0]} x ${times[1]} - ${dataFormatada}</h2>
            <p><strong>Competição:</strong> ${competicao[1]}</p>
            <a href="${gol.matchviewUrl}" target="_blank">Estatísticas</a><br>
            <a href = "${video[3]}">
            <img src="${gol.thumbnail}"width="500" height="300"">
            </a> 
            <br><br>
        `;
        container.appendChild(postDiv);
    });
}
attBtn.onclick(carregarGols(),exibirGols())
