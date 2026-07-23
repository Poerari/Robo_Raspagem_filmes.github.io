# 🎬 Robô de Raspagem de Filmes do Oscar

Este projeto é uma automação em Python desenvolvida para realizar a raspagem de dados (*web scraping*) sobre os filmes indicados e premiados no Oscar, traduzir seus títulos para o português e atualizar automaticamente uma planilha no **Google Sheets**.

---

### 🔗 Links Úteis
> 📊 **[Clique aqui para acessar a Planilha no Google Sheets](https://docs.google.com/spreadsheets/d/1YVmP3By4CyKy6AsURGv5qts0kFdFGKOVkc5cmIUQDvA/edit)**

> 🌐 **[Clique aqui para acessar a fonte dos dados (Scrape This Site)](https://www.scrapethissite.com/pages/ajax-javascript/)**
---

## 🚀 Funcionalidades

* **Raspagem de Dados (Web Scraping):** Coleta informações de filmes indicados ao Oscar por ano (título original, ano de lançamento, indicações, prêmios e se venceu Melhor Filme).
* **Tradução Automática:** Utiliza a API do **TMDb (The Movie Database)** para buscar e traduzir os títulos dos filmes para o português do Brasil (`pt-BR`).
* **Integração com Google Sheets:** Atualiza automaticamente as abas de cada ano na planilha via API do Google Drive e Sheets (`gspread`).
* **Preservação de Formatação:** Atualiza os dados mantendo o layout, cores, cabeçalhos e fórmulas personalizadas (como o ID automático) da planilha intactos.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **[Pandas](https://pandas.pydata.org/):** Manipulação e estruturação dos dados.
* **[Requests](https://requests.readthedocs.io/):** Requisições HTTP para a raspagem e chamadas de API.
* **[gspread](https://docs.gspread.org/):** Integração com a API do Google Sheets.
* **[TMDb API](https://www.themoviedb.org/documentation/api):** Consulta e tradução de títulos de filmes.

---

## ⚙️ Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado e as dependências listadas no projeto:

```bash
pip install pandas requests gspread google-auth
```

2. Configuração das Credenciais
Por razões de segurança, as credenciais da Service Account do Google não estão inclusas neste repositório.

Baixe a sua chave de Conta de Serviço em formato JSON no Google Cloud Console.

Renomeie o arquivo para credentials.json e coloque-o na raiz do projeto.

3. Execução
Rode o script principal pelo terminal:

Bash
python scraper.py
👤 Autora
Desenvolvido por Gabriela Poerari.


---

### 📌 Como atualizar no GitHub:

1. Abra o arquivo **`README.md`** no seu VS Code.
2. Substitua o texto atual por esse modelo acima e salve (`Ctrl + S`).
3. No terminal do VS Code, envie a atualização para o GitHub:

```bash
git add README.md
git commit -m "docs: atualiza README com instrucoes e link da planilha"
git push origin main
```
