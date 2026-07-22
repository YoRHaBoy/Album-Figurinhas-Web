# 🏆 Final Fantasy - Crystal Album

O **Final Fantasy - Crystal Album** é um álbum de figurinhas virtual interativo completo (Frontend + Backend) projetado para homenagear os heróis lendários, conjuradoras, antagonistas, classes clássicas (Jobs) e mascotes de uma das maiores franquias de RPG da história dos videogames. 

Com uma interface imersiva inspirada nos Cristais de Luz, o projeto combina o melhor do web design moderno, animações em SVG/CSS, som sintetizado dinamicamente e uma API RESTful completa desenvolvida com **FastAPI**.

Este projeto foi construído e customizado durante a **Imersão Web & IA** da Alura (julho de 2026).

---

## 🚀 Principais Funcionalidades

### 🎨 Frontend
- **Capa Épica com Cristal de Luz:** Emblema central do Cristal de Luz desenvolvido em SVG vetorial puro, com lapidações em degradê de ciano e safira, aura pulsante de energia Mako, anéis rúnicos 3D orbitais e partículas estelares em movimento.
- **Virada de Página Realista (Page Flip):** Utilização da biblioteca `St.PageFlip` para proporcionar uma experiência fluida e tátil de folhear o álbum de figurinhas.
- **Áudio Sintetizado Dinamicamente (Web Audio API):** Som analógico realista de papel sendo folheado. Gerado 100% via código (White Noise + Bandpass Filter dinâmico com varredura de frequência), dispensando o uso de arquivos externos de áudio.
- **Controle de Som Integrado:** Botão flutuante para alternar o modo com som ou silencioso.
- **Consumo de API Assíncrono:** Comunicação assíncrona (`fetch`) que consulta a API FastAPI para resgatar os metadados das figurinhas e preencher dinamicamente os slots vazios do álbum com as imagens correspondentes.
- **Navegação Flexível:** Suporte a cliques nas setas da interface, arrasto com mouse/touch e atalhos de teclado (`←` e `→`).

### ⚙️ Backend (API RESTful)
- **Servidor FastAPI:** API em Python para listagem de figurinhas e entrega dinâmica de imagens.
- **Suporte a CORS:** Configuração completa de middleware `CORSMiddleware` liberando acessos de qualquer origem (`allow_origins=["*"]`).
- **Resolução de Caminhos Absolutos:** Mapeamento dinâmico de diretórios locais via `os.path.abspath(__file__)`.
- **Busca Inteligente por Glob:** O endpoint de entrega de imagem utiliza `glob.glob` com padronização de prefixos (`{id:02d}[!0-9]*`) para localizar a imagem correta independentemente do nome exato do arquivo.
- **Tratamento de Erros:** Retorno apropriado de status `404 Not Found` caso a imagem solicitada não seja localizada.

---

## 🛠️ Tecnologias Utilizadas

### Frontend
- **Estruturação:** HTML5 Semântico com SVG vetorial inline.
- **Estilização:** CSS3 (Vanilla CSS) com variáveis globais, gradientes radiais/lineares, animações 3D (`@keyframes`) e efeito de texto Glitch.
- **Lógica e Interatividade:** JavaScript Vanilla (ES6+).
- **Biblioteca de Páginas:** [St.PageFlip API](https://github.com/Nodonisko/StPageFlip).
- **Áudio:** Web Audio API (sintetizador analógico de papel).

### Backend
- **Linguagem:** Python 3.10+
- **Framework Web:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Manipulação de Arquivos e Mídia:** `fastapi.responses.FileResponse`, `os`, `glob`
- **Ambiente Virtual:** Python `venv`

---

## 📂 Estrutura do Projeto

```text
/
├── Backend/
│   ├── Imagens/                  # Pasta com as imagens das figurinhas (Formato WebP)
│   │   ├── 01-cloud-strife.webp
│   │   ├── 02-squall-leonheart.webp
│   │   ├── 03-zidane-tribal.webp
│   │   ├── 04-tidus.webp
│   │   └── 05-noctis-lucis.webp
│   ├── main.py                   # Servidor FastAPI e rotas da API
│   └── venv/                     # Ambiente virtual Python
├── Frontend/
│   ├── index.html                # Estrutura HTML das páginas e slots do álbum
│   ├── style.css                 # Estilos visuais, Cristal de Luz em SVG, animações e tema
│   └── app.js                    # Consumo da API, inicialização do PageFlip e som sintetizado
└── README.md                     # Documentação completa do projeto
```

---

## 🌐 Detalhamento dos Arquivos

### 1. ⚙️ [Backend/main.py]
Contém o servidor FastAPI e a API RESTful:
- **`GET /figurinhas`**: Retorna o JSON com a lista das figurinhas cadastradas e ativas no álbum.
- **`GET /figurinhas/{id}/imagem`**: Busca a imagem correspondente ao ID utilizando padrão de busca `glob` e a retorna via `FileResponse` (ou `HTTPException` 404).

### 2. 🎨 [Frontend/index.html]
Contém a estrutura das 8 páginas do álbum:
- **Página 0 (Capa):** Selo de coleção, título em efeito Glitch e a obra central do Cristal de Luz em SVG com partículas e anéis rúnicos.
- **Páginas 1 a 6:** Seções temáticas com slots para as 30 figurinhas (Protagonistas, Heroínas, Vilões, Summons, Jobs e Mascotes).
- **Página 7 (Contracapa):** Resumo do álbum e código de barras.

### 3. 💅 [Frontend/style.css]
Responsável pelo visual de fantasia épica:
- **Cristal de Luz em SVG:** Efeitos de lapidação cristalina, brilho e animação de flutuação.
- **Animações 3D:** Órbitas rúnicas em rotação contínua e partículas de poeira estelar (`.sparkle`).
- **Slots do Álbum:** Bordas dinâmicas indicando o preenchimento da figurinha (`.slot-preenchido`).

### 4. 🧠 [Frontend/app.js]
Gerencia a interatividade e consumo de dados:
- **`preencherFigurinhas()`**: Faz a requisição para `http://localhost:8000/figurinhas` e insere dinamicamente as imagens nos slots correspondentes.
- **`playPaperTurnSound()`**: Sintetizador programático com Web Audio API para reproduzir o som de folhear papel.

---

## ⚡ Como Executar o Projeto

### 1. Iniciar o Backend (FastAPI)

1. Abra o terminal na pasta `Backend`:
   ```bash
   cd Backend
   ```

2. Ative o ambiente virtual (`venv`):
   - **PowerShell:**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Git Bash:**
     ```bash
     source venv/Scripts/activate
     ```
   - **Command Prompt (CMD):**
     ```cmd
     venv\Scripts\activate.bat
     ```

3. Execute o servidor FastAPI com Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   *O servidor estará disponível em:* `http://localhost:8000`

### 2. Abrir o Frontend

Abra o arquivo [Frontend/index.html]  diretamente no seu navegador de preferência ou utilize a extensão **Live Server** do VS Code.

Ao abrir, o frontend irá se conectar automaticamente à API local em `http://localhost:8000/figurinhas` e exibirá as figurinhas disponíveis coladas no álbum!

---

## 📖 Organização das 30 Figurinhas

| ID | Personagem / Item | Categoria | Status na API |
| :---: | :--- | :--- | :---: |
| **01** | Cloud Strife | Protagonistas | 🟢 Ativo |
| **02** | Squall Leonheart | Protagonistas | 🟢 Ativo |
| **03** | Zidane Tribal | Protagonistas | 🟢 Ativo |
| **04** | Tidus | Protagonistas | 🟢 Ativo |
| **05** | Noctis Lucis Caelum | Protagonistas | 🟢 Ativo |
| **06 - 10** | Heroínas (Aerith, Tifa, Yuna, Lightning, Terra) | Heroínas | 🟡 Brevemente |
| **11 - 15** | Vilões (Sephiroth, Kefka, Kuja, Ardyn, Seymour) | Vilões | 🟡 Brevemente |
| **16 - 20** | Summons (Bahamut, Shiva, Ifrit, Odin, Ramuh) | Summons | 🟡 Brevemente |
| **21 - 25** | Jobs (Warrior, Black Mage, White Mage, Dragoon, Thief) | Jobs | 🟡 Brevemente |
| **26 - 30** | Mascotes / Lendas (Chocobo, Moogle, Tonberry, Cactuar, Você) | Mascotes | 🟡 Brevemente |

---

## 📜 Licença

Projeto desenvolvido para fins educacionais durante a Imersão Alura 2026. Todos os direitos dos personagens e marca pertencem à Square Enix.
