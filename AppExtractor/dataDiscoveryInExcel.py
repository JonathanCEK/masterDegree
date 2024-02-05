import pandas as pd
import math
import numpy as np

def processar_planilha(caminho_planilha):
    # Lê a planilha
    df = pd.read_excel(caminho_planilha)

    # Inicializa dicionários para armazenar textos e somas/médias correspondentes
    textos = {}
    somas = {}
    contagens = {}

    # Itera sobre as linhas do DataFrame
    for index, row in df.iterrows():
        texto = row['45']
        numero = row['50']

        # Se o texto já existe, atualiza a soma e a contagem
        if texto in textos:
            somas[texto] += numero
            contagens[texto] += 1
        # Se o texto é novo, cria entradas nos dicionários
        else:
            textos[texto] = True
            somas[texto] = numero
            contagens[texto] = 1

    # Inicializa um dicionário para armazenar as médias
    medias = {}

    # Calcula as médias
    for texto in textos:
        medias[texto] = somas[texto] / contagens[texto]

    return medias

# Exemplo de uso
caminho_arquivo_excel = "F:\\Projetinhos\\Projeto Dissertação\\PythonColetaDados\\totalInfoComplete.xlsx"
#resultados = processar_planilha(caminho_arquivo_excel)


df = pd.read_excel(caminho_arquivo_excel, skiprows=1)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def gerar_nuvem_de_palavras(texto):
    # Configuração da WordCloud
    cores = {'python': 'red', 'data': 'blue', 'cloud': 'green', 'word': 'orange'}
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)
    wordcloud.recolor(color_func=lambda palavra, _: cores.get(palavra.lower(), 'black'))
    # Exibição da nuvem de palavras usando Matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Exemplo de uso
#texto_exemplo = "Python é uma linguagem de programação poderosa e versátil. É amplamente usada em desenvolvimento web, análise de dados e aprendizado de máquina."
coluna_limpa = df['Positive Reviews Examples'].dropna()

# Verifique se a coluna não está vazia antes de criar a string
if not coluna_limpa.empty:
    positive = coluna_limpa.to_string(index=False)
#positive = df['Positive Reviews Examples'].to_string(index=False)
# Gere a nuvem de palavras
gerar_nuvem_de_palavras(positive)


#print(df['Permission:Development tools'].isnull().sum())

## Conta os valores únicos na coluna 'appDeveloper' e pega os 5 mais frequentes
#top_desenvolvedores = df['Developer'].value_counts()
#unique_developers = df['Developer'].value_counts()
#unique_developers_single_occurrence = unique_developers[unique_developers == 3]
#
#print("Top 5 desenvolvedores:")
#print(len(unique_developers_single_occurrence))
#
#
# Arredonda os valores da coluna 'Rating' e conta a frequência de cada valor
#df['User Rating'] = df['User Rating'].apply(lambda x: math.floor(float(x)))

#df['User Rating'] = df['User Rating'].apply(lambda x: round(x * 2) / 2 if pd.notna(x) else 'N/A')
#df['User Rating'] = np.floor(df['User Rating'] + 0.5).astype(int).replace({0: 'N/A'})
#rating_arredondado = df['User Rating'].value_counts()
#print("Frequência de cada Rating arredondado:")
#print(rating_arredondado)

# Agrupa por categoria e soma os downloads
#total_downloads_por_categoria = df.groupby('appCategory')['Total downloads'].median()

#total_downloads_por_categoria[0]

# Exibe o total de downloads por categoria

#for i in total_downloads_por_categoria:
#    print(i)

#print(total_downloads_por_categoria)

#print(media_por_categoria)
# Exibe as médias calculadas
#for texto, media in resultados.items():
#    print(f'Texto: {texto}, Média: {media}')


#from collections import Counter
#
## Combine todas as linhas da coluna "Technologie:Development tools"
#todas_ferramentas = '\n'.join(df['Technologie:Development tools'].dropna())
#
## Divida a string combinada em linhas e conte a frequência de cada ferramenta
#contagem_ferramentas = Counter(todas_ferramentas.split('\n'))
#
## Obtenha as 6 ferramentas mais comuns
#top_ferramentas = contagem_ferramentas.most_common(6)
#
#print("As 6 ferramentas mais usadas:")
#for ferramenta, contagem in top_ferramentas:
#    print(f"{ferramenta}: {contagem} vezes")



#from collections import Counter
#
## Combine todas as linhas das colunas que começam com "Permission:"
#todas_ferramentas = ''
#for coluna in df.columns:
#    if coluna.startswith("Permission:"):
#        todas_ferramentas += '\n'.join(df[coluna].dropna()) + '\n'
#
## Divida a string combinada em linhas e conte a frequência de cada ferramenta
#contagem_ferramentas = Counter(todas_ferramentas.split('\n'))
#
## Obtenha as 6 ferramentas mais comuns
#top_ferramentas = contagem_ferramentas.most_common(12)
#
#print("As 6 ferramentas mais usadas nas colunas com prefixo 'Permission:':")
#for ferramenta, contagem in top_ferramentas:
#    print(f"{ferramenta}: {contagem} vezes")

    