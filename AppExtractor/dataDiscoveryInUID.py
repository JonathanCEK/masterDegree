import pandas as pd
import math
import numpy as np


# Exemplo de uso
caminho_arquivo_excel = "F:\\Projetinhos\\Projeto Dissertação\\PythonColetaDados\\ColetaSucesso.xlsx"
#resultados = processar_planilha(caminho_arquivo_excel)


df = pd.read_excel(caminho_arquivo_excel)

def restrictions ():

    temp = df['Não disponível na GPlay'].value_counts()
    print("Não disponível na GPlay")
    print(temp)
    temp = df['Incompatível com o dispositivo emulado (GPlay)'].value_counts()
    print("Incompatível com o dispositivo emulado (GPlay)")
    print(temp)
    temp = df['Jogo'].value_counts()
    print("Jogo")
    print(temp)
    temp = df['Acesso somente com número telefônico'].value_counts()
    print("Acesso somente com número telefônico")
    print(temp)
    temp = df['Funcionamento restrito por região'].value_counts()
    print("Funcionamento restrito por região")
    print(temp)
    temp = df['Somente em Landscape'].value_counts()
    print("Somente em Landscape")
    print(temp)
    temp = df['Volume de dados grande (Download)'].value_counts()
    print("Volume de dados grande (Download)")
    print(temp)
    temp = df['Não permitir Screenshots nas páginas principais ou totalmente'].value_counts()
    print("Não permitir Screenshots nas páginas principais ou totalmente")
    print(temp)
    temp = df['Interface Gráfica mínima ou não útil (Game,Launcher,Keyboard, API...)'].value_counts()
    print("Interface Gráfica mínima ou não útil (Game,Launcher,Keyboard, API...)")
    print(temp)
    temp = df['Língua distinta da inglesa'].value_counts()
    print("Língua distinta da inglesa")
    print(temp)
    temp = df['Funcionamento Incorreto'].value_counts()
    print("Funcionamento Incorreto")
    print(temp)
    temp = df['Impedimentos no cadastro (sem considerar telefone)'].value_counts()
    print("Impedimentos no cadastro (sem considerar telefone)")
    print(temp)
    temp = df['Incompatível com o dispositivo emulado (App)'].value_counts()
    print("Incompatível com o dispositivo emulado (App)")
    print(temp)
    temp = df['Pago'].value_counts()
    print("Pago")
    print(temp)
    temp = df['Descartados por excesso'].value_counts()
    print("Descartados por excesso")
    print(temp)
#print(df['Permission:Development tools'].isnull().sum())

temp = df['Color'].value_counts()

#print(temp)
    

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def gerar_nuvem_de_palavras(texto):
    # Configuração da WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)

    # Exibição da nuvem de palavras usando Matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Exemplo de uso
#texto_exemplo = "Python é uma linguagem de programação poderosa e versátil. É amplamente usada em desenvolvimento web, análise de dados e aprendizado de máquina."

positive = df['']
# Gere a nuvem de palavras
gerar_nuvem_de_palavras(texto_exemplo)

## Conta os valores únicos na coluna 'appDeveloper' e pega os 5 mais frequentes
#top_desenvolvedores = df['Developer'].value_counts()
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

    