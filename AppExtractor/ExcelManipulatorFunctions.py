import requests
import pandas as pd
import pyperclip
import time
import openpyxl

#from requests_html import HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def setPlayStore(url1):

    diretorio = ""
    playstore = ""
    partes = url1.split('/')
    # Verifica se existem pelo menos quatro ocorrências de "/"
    if len(partes) >= 6:
        # Retorna o texto após a quarta ocorrência
        diretorio = '/'.join(partes[5:])
        playstore = 'https://play.google.com/store/apps/details?id=' + diretorio
        print(diretorio)
    else:
        # Se não houver quatro ocorrências, retorne uma string vazia ou outra mensagem de erro, conforme necessário
        print("Erro")

    return [diretorio, playstore]

def extrair_caracteristicas(string):
    # Lista de características
    caracteristicas = [
        "More data about",
        "Price",
        "Cost of in-app purchases",
        "Total downloads",
        "Recent downloads",
        "Rating",
        "Ranking",
        "Version",
        "APK size",
        "Number of libraries",
        "Designed for",
        "Maturity",
        "Suitable for",
        "Ads"
    ]

    # Inicializa o vetor de valores com "N/A"
    valores = ["N/A"] * 14

    # Divide a string em linhas
    linhas = string.split('\n')
    
    # Para cada linha, verifica se corresponde a alguma característica e extrai o valor
    for linha in linhas:
        for i, caracteristica in enumerate(caracteristicas):
            if linha.startswith(caracteristica):
                # Extrai o valor removendo a parte da característica
                valores[i] = linha[len(caracteristica):].strip()

    return valores

def separate_tech(string):

    # Divide a string em linhas
    linhas = string.split('\n')

    tech = False

    strPerm = ""
    strTech = ""
    
    # Para cada linha, verifica se corresponde a alguma característica e extrai o valor
    for linha in linhas:
        if tech:
            strTech = strTech + linha + "\n"
        else : 
            if linha.startswith("Technologies used by "):
                tech = True
            else: 
                strPerm = strPerm + linha + "\n"
    
    if len(strTech) == 0:
        strTech = "N/A"

    if len(strPerm) == 0:
        strPerm = "N/A"
    
    return [strPerm, strTech]


def rating(string):
    valores = []

    if string != 'No ratings':
        valores = string.split(' based on ')
        valores[1] = valores[1].replace(' ratings', '')

    return valores

def noAndroid(string):
    text =  []
    if string.startswith('Android '):
        text.append(string.replace('Android ', ''))
        text[0] = text[0].replace('+', '')
    return text

def noPerm(string):
    string[0]
    if string.startswith('N/A'):
        return string
    else:
        string

def remover_primeira_linha(texto):
    linhas = texto.split('Development tools\n', 1)
    if len(linhas) > 1:
        return [linhas[0]]
    else:
        return ['N/A']


def processar_linhas_pares(texto, lista_geral):
    linhas = texto.split('\n')
    
    # Adiciona o texto das linhas pares à lista geral
    for i in range(0, len(linhas), 2):
        texto_linha_par = linhas[i].strip()  # Remove espaços em branco no início e no final
        if texto_linha_par not in lista_geral:
            lista_geral.append(texto_linha_par)


def processar_string(string, lista_fixa):
    # Inicializa a lista com "N/A"
    lista_resultado = ["N/A"] * 12

    # Divide a string em linhas
    linhas = string.split('\n')

    # Itera pelas linhas pares
    for i in range(0, len(linhas), 2):
        texto_linha_par = linhas[i].strip()  # Remove espaços em branco no início e no final

        # Verifica se o texto da linha par corresponde a algum elemento da lista fixa
        if texto_linha_par in lista_fixa:
            # Encontra a posição na lista fixa
            posicao = lista_fixa.index(texto_linha_par)

            # Se a próxima linha existe (linha ímpar), atribui à lista resultado
            if i + 1 < len(linhas):
                lista_resultado[posicao] = linhas[i + 1].strip()

    return lista_resultado

def offOrganizer():

    #service = Service()
    #options = webdriver.EdgeOptions()
    #options.add_argument("--headless") #não renderiza interface gráfica
    #driver = webdriver.Edge(service=service, options=options)
    # Nome do arquivo Excel a ser lido e atualizado
    path = "F:\\Projetinhos\\Projeto Dissertação\\PythonColetaDados\\"
    nome = "totalInfoComplete"
    extension = ".xlsx"

    linhaInicial = 3
    countLinha = linhaInicial
    
    finalValue = 1

    selectCol = 29
    firtWritingCol = 33




    #inicialmente ele abre um app com acesso restrito, apenas para deixar sinalizado que quero acessar esses apps
    #driver.get('https://www.appbrain.com/app/beechat-dating-nearby/th.cyberapp.beechat')
    #time.sleep(5)

    # Abre o arquivo Excel
    workbook = openpyxl.load_workbook(path + nome + extension)
    sheet = workbook.active

    lista_geral = ['Development tools', 'Network communication', 'Storage', 'Hardware controls', 'System tools',  'Your accounts', 'Your location', 'Your personal information', 'Phone calls', 'Services that cost you money', 'Your messages', 'Extra']

    # Itera pelas linhas na primeira coluna do arquivo Excel
    for row in sheet.iter_rows(min_row=linhaInicial, max_row=sheet.max_row, min_col=selectCol, max_col=selectCol):
        if countLinha == finalValue: break
        for cell in row:
            texto = cell.value
            countLinha = countLinha + 1
            #print(texto)
            if texto is not None:
                # Obtém os valores da função processarTexto
                #valores = extrair_caracteristicas(texto)
                #valores = remover_primeira_linha(texto)
                valores = processar_string(texto, lista_geral)

                #looping para adicionar os elementos em valores às colunas da tabela
                for i, val in enumerate(valores, start=firtWritingCol):
                    sheet.cell(row=cell.row, column=i, value=val)

                #print(countLinha)

    # Salva as alterações de volta no arquivo Excel
    workbook.save(path + nome + extension)
    print(lista_geral)
    print("Organização finalizada.")


offOrganizer()
    




