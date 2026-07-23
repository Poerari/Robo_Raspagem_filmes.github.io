import pandas as pd
import gspread
import requests
import traceback
import time

API_KEY = "63eb2e797fc12673b7c6303fea5431a6"

from google.oauth2.service_account import Credentials

def traduzir_titulo_tmdb(titulo, ano):
    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": API_KEY,
        "query": titulo,
        "year": ano,
        "language": "pt-BR"
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()

        resultados = resposta.json().get("results", [])

        if resultados:
            return resultados[0]["title"]

    except Exception as e:
        print(f"Erro ao traduzir '{titulo}': {e}")

    return titulo


def raspar_dados_ano(ano):
    print(f"\n--- Buscando filmes de {ano} ---")

    url = "https://www.scrapethissite.com/pages/ajax-javascript/"

    resposta = requests.get(
        url,
        params={
            "ajax": "true",
            "year": ano
        },
        timeout=30
    )

    resposta.raise_for_status()

    filmes = resposta.json()

    if not filmes:
        print("Nenhum filme encontrado.")
        return [], []

    cabecalhos = [
        "Título",
        "Ano",
        "Indicações",
        "Prêmios",
        "Melhor Filme"
    ]

    dados = []

    for filme in filmes:
        titulo_pt = traduzir_titulo_tmdb(
            filme.get("title", "").strip(),
            filme.get("year")
        )

        dados.append([
            titulo_pt,
            filme.get("year", ""),
            filme.get("nominations", ""),
            filme.get("awards", ""),
            "Sim" if filme.get("best_picture", False) else "Não"
        ])

    print(f"Foram encontrados {len(dados)} filmes.")

    return cabecalhos, dados


def salvar_no_sheets(planilha, ano, cabecalhos, dados):
    if not dados:
        return

    print(f"Salvando dados na aba '{ano}'...")

    try:
        aba = planilha.worksheet(str(ano))
    except gspread.exceptions.WorksheetNotFound:
        aba = planilha.add_worksheet(title=str(ano), rows="100", cols="20")
        # Se a aba for nova, cria o título e o cabeçalho igual ao modelo
        aba.update(range_name="A1", values=[["Filmes Indicados ao Oscar"]])
        aba.merge_cells("A1:F1")
        aba.update(range_name="A2", values=[["ID", "Título", "Ano", "Indicações", "Prêmios", "Melhor Filme"]])

    # 1. Limpa APENAS o intervalo dos dados antigos (B3:F100),
    #    sem tocar no título, no cabeçalho nem na coluna A (ID com fórmula)
    aba.batch_clear(["B3:F100"])

    # 2. Escreve os filmes novos a partir de B3, preservando toda a formatação
    aba.update(range_name="B3", values=dados)

    print(f"✅ Sucesso! Dados de {ano} preenchidos sem alterar a formatação.")


def iniciar_robo():
    print("Conectando ao Google Sheets...")

    escopos = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    credenciais = Credentials.from_service_account_file("credentials.json", scopes=escopos)
    gc = gspread.authorize(credenciais)
    print(gc.openall())

    PLANILHA_ID = "1YVmP3By4CyKy6AsURGv5qts0kFdFGKOVkc5cmIUQDvA"

    try:
        planilha = gc.open_by_key(PLANILHA_ID)
        print("✅ Conectado à planilha com sucesso!")
    except Exception:
        traceback.print_exc()
        return

    anos = [2014, 2015]

    for ano in anos:
        cabecalhos, dados = raspar_dados_ano(ano)
        salvar_no_sheets(planilha, ano, cabecalhos, dados)
        time.sleep(2)


if __name__ == "__main__":
    iniciar_robo()