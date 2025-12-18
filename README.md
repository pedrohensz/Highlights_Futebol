Um site simples e elegante que exibe os melhores gols e highlights de futebol do mundo todo, atualizados em tempo real a partir da API do Scorebat.

## ✨ Funcionalidades

- Exibição dos highlights de gols mais recentes de diversas competições
- Thumbnail clicável que abre o vídeo diretamente
- Informações claras: placar, data (formatada em pt-BR), competição
- Link para estatísticas completas do jogo
- Botão "Atualizar Feed" para recarregar os dados mais recentes
- Design limpo, centralizado e com boa legibilidade

## 🖥️ Tecnologias utilizadas

### Frontend
- HTML5
- CSS3
- JavaScript vanilla (sem frameworks)

### Backend
- **FastAPI** (Python)
- Proxy para evitar problemas de CORS ao consumir a API do Scorebat
- Deploy gratuito no **Railway**

### APIs externas
- [Scorebat Video API](https://www.scorebat.com/video-api/) – fonte principal dos highlights


## 📂 Estrutura do projeto
.
├── index.html     # Página principal
├── style.css      # Estilos da aplicação
├── script.js      # Lógica de carregamento e exibição dos gols
├── main.py        # Backend FastAPI (proxy)
└── README.md      # Este arquivo
text## 🚀 Como rodar localmente

### Backend (FastAPI)

1. Crie e ative um ambiente virtual (recomendado):
   # Linux/Mac
   python -m venv venv
   source venv/bin/activate    
   #ou
   # Windows
   venv\Scripts\activate      

Instale as dependências:
pip install fastapi uvicorn requests
Crie um arquivo .env na raiz com sua chave da Scorebat:textkey=SUA_CHAVE_SCOREBAT_AQUI
Inicie o servidor:
uvicorn main:app --reloadO backend ficará disponível em http://127.0.0.1:8000

Frontend
Como é apenas arquivos estáticos, abra o index.html diretamente no navegador ou sirva com um servidor local:
python -m http.server 8080
Acesse em http://localhost:8080
Para testes locais, altere a constante API em script.js para:JavaScriptconst API = "http://127.0.0.1:8000";
🌍 Deploy atual

Backend (FastAPI): https://highlightsfutebol-production.up.railway.app
Frontend servido estaticamente (pode ser hospedado no Netlify, Vercel, GitHub Pages, etc.)

🔧 Possíveis melhorias futuras

Aceito Sugestões

👤 Autor
Pedro Henrique (pedrohensz)
Dúvidas, sugestões ou contribuições? Abra uma issue ou entre em contato!

Aproveite os gols mais bonitos do planeta! ⚽
textPronto! É só salvar esse conteúdo como `README.md` no seu repositório. Fica bonito no GitHub e deixa o projeto bem documentado. 

