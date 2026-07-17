# 🏆 Final Fantasy - Crystal Album

O **Final Fantasy - Crystal Album** é um álbum de figurinhas virtual interativo projetado e desenvolvido para homenagear os personagens icônicos, conjuradoras, antagonistas, classes clássicas (Jobs) e mascotes lendários de uma das maiores franquias de RPG da história dos videogames. Com uma interface inspirada em cristais mágicos, efeitos visuais refinados e transições de página realistas, o projeto combina o melhor do web design moderno e da interatividade frontend.

Este projeto foi customizado a partir do projeto base construído durante a **Imersão Alura** de julho de 2026.

---

## 🚀 Principais Funcionalidades

- **Virada de Página Realista (Page Flip):** Utiliza a biblioteca `St.PageFlip` para proporcionar uma experiência snappier e tátil de folhear as páginas do álbum.
- **Controles de Navegação Flexíveis:** Navegação fluida por meio de botões visuais na tela, cliques/arrastes do mouse/tela touch, ou usando as setas do teclado (`←` e `→`).
- **Áudio Sintetizado Dinamicamente (Web Audio API):** Som realista de papel sendo folheado. Em vez de carregar arquivos de áudio externos grandes, o sistema gera o som dinamicamente via sintetizador do navegador (White Noise com filtros dinâmicos e envelopes de volume).
- **Controle de Som:** Botão flutuante para alternar o modo silencioso ou ativado.
- **Consumo de API Dinâmica:** Integração automática com um backend para carregar dinamicamente imagens de figurinhas do servidor e preencher os slots vazios correspondentes.
- **Visual Premium:** Design com tema de fantasia e cristais (Dark Mode), paleta de cores azul cristalina e Mako, efeitos de brilho (glow), glassmorphism, importação de fontes serif majestosas (`Cinzel`) e efeito de texto glitch na capa.

---

## 🛠️ Tecnologias Utilizadas

- **Estruturação:** HTML5 semântico
- **Estilização:** CSS3 (Vanilla CSS) com variáveis globais, gradientes radiais, layouts flex e grid responsivos.
- **Interatividade:** JavaScript Vanilla (ES6+)
- **Efeitos de Página:** [St.PageFlip API](https://github.com/Nodonisko/StPageFlip)
- **Sintetizador de Áudio:** Web Audio API (geração de ondas sonoras programáticas)
- **Integração:** Fetch API para comunicação com servidor RESTful

---

## 📂 Detalhamento dos Arquivos e Suas Funções

O projeto é composto por três arquivos fundamentais na raiz, cada um responsável por uma camada específica da aplicação:

### 1. 🌐 Estruturação e Conteúdo — [index.html](file:///c:/Users/bruno/OneDrive/Desktop/Imersoes%20Alura/Imersao%20Arq%20Web%20IA/index.html)
Este arquivo define o esqueleto semântico da aplicação e contém todos os dados estruturais do álbum:
*   **Controles de UI Iniciais:** Contém o botão de controle de áudio (`#sound-toggle`) com ícones SVG alternáveis e as setas de navegação (`#btn-prev` e `#btn-next`).
*   **Contêiner do Livro (`.album-viewport` e `#book`):** A estrutura que envolve as páginas do álbum. Cada página é representada por uma `div` com a classe `.page` e atributos específicos como `data-density="hard"` para as capas duras.
*   **Templates de Grade das Figurinhas (`.stickers-grid`):** Estrutura interna de cada página temática com slots (`.sticker-slot`), contendo o número do slot (`.slot-number`), o nome do personagem (`.slot-name`) e o seu papel/jogabilidade de origem (`.slot-role`).
*   **Carregamento de Scripts:** Importa a biblioteca externa `page-flip.browser.min.js` via CDN e o script de comportamento local [app.js](file:///c:/Users/bruno/OneDrive/Desktop/Imersoes%20Alura/Imersao%20Arq%20Web%20IA/app.js).

### 2. 🎨 Estilização e Efeitos Visuais — [style.css](file:///c:/Users/bruno/OneDrive/Desktop/Imersoes%20Alura/Imersao%20Arq%20Web%20IA/style.css)
Responsável por criar a atmosfera mágica de fantasia épica e cristais (Cyberpunk/Sci-Fi/RPG) através de técnicas modernas de CSS:
*   **Variáveis CSS (Custom Properties):** Centraliza as cores do tema de cristais (como `--color-blue-universe`, `--color-deep-blue` e `--color-dev-blue`) para manter a coerência visual.
*   **Layouts e Alinhamentos:** Utiliza `Flexbox` para centralização do álbum na tela e `Grid` para a disposição geométrica simétrica dos slots de figurinhas dentro das páginas.
*   **Animações e Efeitos Complexos:**
    *   **Glitch Effect:** Animação de texto na capa simulando interferência digital e instabilidade da energia de Gaia.
    *   **3D Tech Sphere:** Criação de anéis rotativos tridimensionais iluminados na capa utilizando `keyframes` de rotação em 3D.
    *   **Efeito Hover e Glassmorphism:** Botões e slots translúcidos com bordas brilhantes ativadas sob o cursor.
*   **Responsividade:** Controle dinâmico das dimensões do livro e ocultação de controles para se adaptar a diferentes tamanhos de tela.

### 3. 🧠 Inteligência e Comportamento — [app.js](file:///c:/Users/bruno/OneDrive/Desktop/Imersoes%20Alura/Imersao%20Arq%20Web%20IA/app.js)
Controla toda a lógica dinâmica, integração de APIs e som:
*   **Integração com Backend API (`preencherFigurinhas`):**
    *   Realiza uma requisição assíncrona (`fetch`) para obter os metadados das figurinhas a partir de `API_BASE_URL` (`http://localhost:8000/figurinhas`).
    *   Cria um mapeamento (`Map`) e varre todos os slots do HTML.
    *   Cria elementos `<img>` dinamicamente para as figurinhas cujos IDs foram encontrados e injeta-os no DOM, ativando a classe `.slot-preenchido` ao carregar a imagem com sucesso.
*   **Inicialização do St.PageFlip:** Configura propriedades como tamanho máximo e mínimo de página, sombras dinâmicas (`drawShadow`), suporte a gestos mobile e tempo de transição otimizado para 800ms.
*   **Gestos de Arraste Customizados:** Implementa ouvintes manuais de eventos de mouse (`mousedown`, `mousemove`, `mouseup`) e touch (`touchstart`, `touchmove`, `touchend`) para criar uma transição de dobra suave que acompanha a posição do dedo ou cursor.
*   **Sintetizador Programático de Áudio (`playPaperTurnSound`):**
    *   Cria um buffer de áudio temporário com ruído branco.
    *   Desenha uma curva de volume (Envelope AD) para emular o início rápido da virada e o decaimento suave.
    *   Aplica um **Bandpass Filter** (Filtro Passa-Faixa) dinâmico com varredura de frequência exponencial (de 1500Hz para 350Hz) para recriar o "whoosh" do ar sendo deslocado pelo papel.
    *   Conecta tudo ao canal de saída de som do dispositivo do usuário.
*   **Interações com a Interface:** Atalhos por teclado (`←` e `→`), desabilitação e habilitação dinâmica das setas laterais com base na página atual (esconde no início e fim do álbum).

---

## 📖 Organização das Páginas e Categorias

O álbum é dividido em seções temáticas muito bem detalhadas:

*   **Página 0 (Capa):** Título estilizado com efeito *Glitch*, colagem de silhuetas de figurinhas flutuantes e esfera cristalina 3D central.
*   **Página 1 (Protagonistas):** Guerreiros da Luz clássicos como Cloud Strife, Squall Leonhart, Zidane Tribal, Tidus e Noctis Lucis Caelum.
*   **Página 2 (Heroínas):** Conjuradoras e guerreiras de grande destaque, incluindo Aerith Gainsborough, Tifa Lockhart, Yuna, Lightning e Terra Branford.
*   **Página 3 (Vilões):** Antagonistas e vilões marcantes como Sephiroth, Kefka Palazzo, Kuja, Ardyn Izunia e Seymour Guado.
*   **Página 4 (Summons):** Divindades lendárias e evocações clássicas como Bahamut, Shiva, Ifrit, Odin e Ramuh.
*   **Página 5 (Jobs):** Classes clássicas da franquia, incluindo Guerreiro (Warrior), Mago Negro (Black Mage), Mago Branco (White Mage), Dragoneiro (Dragoon) e Ladrão (Thief).
*   **Página 6 (Mascotes):** Criaturas lendárias do universo RPG como Chocobo, Moogle, Tonberry, Cactuar e o lendário Guerreiro da Luz (Você!).
*   **Página 7 (Contracapa):** Resumo do álbum com logotipo oficial e código de barras simulado.

---

## ⚙️ Como Executar o Projeto

### 1. Inicializar o Frontend
Como o frontend é composto de arquivos estáticos, basta abrir o arquivo [index.html](file:///c:/Users/bruno/OneDrive/Desktop/Imersoes%20Alura/Imersao%20Arq%20Web%20IA/index.html) diretamente no seu navegador, ou utilizar uma extensão como o *Live Server* do VS Code para executá-lo sob um servidor local.

### 2. Inicializar o Backend (Para Carregamento das Figurinhas)
Para que as figurinhas apareçam preenchidas nos slots em vez de mostrarem apenas o número e descrição:
1. Certifique-se de que o servidor backend está rodando no endereço local: `http://localhost:8000`.
2. O servidor padrão é baseado em FastAPI. Para rodá-lo, navegue até a pasta do backend e execute:
   ```bash
   cd backend/dia-3
   uvicorn main:app --reload
   ```
3. O script [app.js](file:///c:/Users/bruno/OneDrive/Desktop/Imersoes%20Alura/Imersao%20Arq%20Web%20IA/app.js) detectará automaticamente a conexão e substituirá os slots cinzas pelas fotos oficiais dos personagens.

---

## 🎵 O Efeito de Som de Papel Sintetizado

Um dos destaques de engenharia de software no projeto é a função `playPaperTurnSound()` presente no [app.js](file:///c:/Users/bruno/OneDrive/Desktop/Imersoes%20Alura/Imersao%20Arq%20Web%20IA/app.js). Ela utiliza a **Web Audio API** para simular o atrito das páginas:
- **Gerador de Ruído:** Um buffer de ruído branco (White Noise) é criado dinamicamente em tempo de execução.
- **Envelope de Ganho:** Um envelope AD (Attack-Decay) faz o volume subir rapidamente e cair de forma suave simulando a aceleração da página.
- **Filtro Dinâmico:** Um filtro passa-faixa (Bandpass Filter) com uma varredura de frequência exponencial que decai de 1500Hz a 350Hz imita o efeito de distanciamento sonoro da folha ao ser virada.
- **Filtro Passa-Baixo:** Remove frequências agudas metálicas indesejadas para soar o mais analógico possível.
