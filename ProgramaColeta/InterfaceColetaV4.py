import tkinter as tk
from tkinter import ttk
import pyperclip
import os
from datetime import datetime

diretorio_screenshots = "F:\\Projetinhos\\Projeto Dissertação\\Screenshots"
diretorio_registro = "registro\\"
set_register_on_lauch = False
pre_select_features = True

class Componente:
    imagens = []  # Lista para manter referências às imagens

    def __init__(self, master, texto, imagem_path, row, column):
        self.checkbox_var = tk.BooleanVar()
        
        # Carregar a imagem e armazenar a referência
        imagem = tk.PhotoImage(file=imagem_path)
        self.imagens.append(imagem)
        self.imageview = ttk.Label(master, image=imagem, compound=tk.TOP)
        self.checkbox = ttk.Checkbutton(master, variable=self.checkbox_var)
        self.textview = ttk.Label(master, text=texto)
        #if(row  != 10):
        #    self.imageview.grid(row=row+2, column=column, padx=0, pady=0)
#
        #if row != 11 and not ((row == 8 and column in [7, 8]) or (row == 10 and column in [0, 1, 2])):
        #    self.checkbox.grid(row=row + 1, column=column, pady=0, padx=15, sticky="w")  
        #    self.textview.grid(row=row + 1, column=column, pady=0, padx=35, sticky="w") 
        self.imageview.grid(row=row+2, column=column, padx=0, pady=0)
        self.checkbox.grid(row=row + 1, column=column, pady=0, padx=15, sticky="w")  
        self.textview.grid(row=row + 1, column=column, pady=0, padx=35, sticky="w")

        # Adiciona um evento de clique à imagem / texto para acionar o checkbox
        self.imageview.bind("<Button-1>", lambda event: self.acionar_checkbox())
        self.textview.bind("<Button-1>", lambda event: self.acionar_checkbox())

    # evento para acionar o checkbox
    def acionar_checkbox(self):
        # Inverte o estado da checkbox ao ser clicado na imagem
        self.checkbox_var.set(not self.checkbox_var.get())

# Crie a janela principal
janela = tk.Tk()
janela.title("Programa para coleta")

# Substitua os caminhos reais das imagens e os textos desejados
dados_componentes = [
    #
    #Raramente marcados - Line 1
    {"texto": "Pre-Loading", "imagem_path": "imagensPrograma\\imagem_acc.png"},
    {"texto": "Badges", "imagem_path": "imagensPrograma\\imagem_bad.png"},
    {"texto": "Snackbar", "imagem_path": "imagensPrograma\\imagem_25.png"},
    {"texto": "Tool tips", "imagem_path": "imagensPrograma\\imagem_30.png"},    
    {"texto": "Extended FAB", "imagem_path": "imagensPrograma\\imagem_exfab.png"},
    {"texto": "Floating Action Buttons", "imagem_path": "imagensPrograma\\imagem_fab.png"},
    {"texto": "Botton app bar", "imagem_path": "imagensPrograma\\imagem_1.png"},
    {"texto": "Web view", "imagem_path": "imagensPrograma\\imagem_web.png"},
    {"texto": "Music", "imagem_path": "imagensPrograma\\imagem_mus.png"},
    #
    #Poucas vezes marcados  - Line 2
    {"texto": "Date pickers", "imagem_path": "imagensPrograma\\imagem_12.png"},
    {"texto": "Time picker dial", "imagem_path": "imagensPrograma\\imagem_dia.png"},
    {"texto": "Time picker input", "imagem_path": "imagensPrograma\\imagem_29.png"},
    {"texto": "Radio button", "imagem_path": "imagensPrograma\\imagem_21.png"},
    {"texto": "Switch", "imagem_path": "imagensPrograma\\imagem_26.png"},
    {"texto": "Checkbox", "imagem_path": "imagensPrograma\\imagem_9.png"},
    {"texto": "Sliders", "imagem_path": "imagensPrograma\\imagem_24.png"},
    {"texto": "Map View", "imagem_path": "imagensPrograma\\imagem_map.png"},
    {"texto": "Video View", "imagem_path": "imagensPrograma\\imagem_vid.png"},
    #
    #De vez em quando marcados  - Line 3
    {"texto": "Segmented Buttons", "imagem_path": "imagensPrograma\\imagem_seg.png"},
    {"texto": "Chips", "imagem_path": "imagensPrograma\\imagem_10.png"},
    {"texto": "Primary tabs", "imagem_path": "imagensPrograma\\imagem_27.png"},
    {"texto": "Secondary tabs", "imagem_path": "imagensPrograma\\imagem_sec.png"},
    {"texto": "Bottom sheets", "imagem_path": "imagensPrograma\\imagem_22.png"},
    {"texto": "Side sheets", "imagem_path": "imagensPrograma\\imagem_23.png"},
    {"texto": "Menus", "imagem_path": "imagensPrograma\\imagem_17.png"},
    {"texto": "Progress indicators (horizontal)", "imagem_path": "imagensPrograma\\imagem_20.png"},
    {"texto": "Progress indicators analogico", "imagem_path": "imagensPrograma\\imagem_ana.png"},
    #
    # Frequentemente marcados - Line 4
    {"texto": "Acccount", "imagem_path": "imagensPrograma\\imagem_acc.png"},
    {"texto": "Noturno", "imagem_path": "imagensPrograma\\imagem_dark.png"},
    {"texto": "Paisagem", "imagem_path": "imagensPrograma\\imagem_pai.png"},   
    {"texto": "Sound Effects", "imagem_path": "imagensPrograma\\imagem_sound.png"},
    {"texto": "Social", "imagem_path": "imagensPrograma\\imagem_social.png"},
    {"texto": "Text field", "imagem_path": "imagensPrograma\\imagem_28.png"},
    {"texto": "Search", "imagem_path": "imagensPrograma\\imagem_ser.png"},
    {"texto": "Dialog", "imagem_path": "imagensPrograma\\imagem_13.png"},
    {"texto": "Dialog full-screen", "imagem_path": "imagensPrograma\\imagem_fls.png"},
    #
    #Muitas vezes marcados  - Line 5
    {"texto": "Navigation rail", "imagem_path": "imagensPrograma\\imagem_19.png"},
    {"texto": "Navigation drawer", "imagem_path": "imagensPrograma\\imagem_18.png"},
    {"texto": "Navigation bar", "imagem_path": "imagensPrograma\\imagem_5.png"},
    {"texto": "Top app bar", "imagem_path": "imagensPrograma\\imagem_2.png"},
    {"texto": "Cards", "imagem_path": "imagensPrograma\\imagem_8.png"},
    {"texto": "MultiCard", "imagem_path": "imagensPrograma\\imagem_cards.png"},
    {"texto": "Carousel", "imagem_path": "imagensPrograma\\imagem_car.png"},
    {"texto": "Divider", "imagem_path": "imagensPrograma\\imagem_14.png"},
    {"texto": "Lists", "imagem_path": "imagensPrograma\\imagem_16.png"},
    #
    #pre-marcados  - Line 6
    {"texto": "Common buttons", "imagem_path": "imagensPrograma\\imagem_6.png"},
    {"texto": "Icon Buttons", "imagem_path": "imagensPrograma\\imagem_btt.png"},
    {"texto": "Text View", "imagem_path": "imagensPrograma\\imagem_text.png"},
    {"texto": "Image View", "imagem_path": "imagensPrograma\\imagem_im.png"},



    
    
    
]

# Variáveis para organizar as colunas
max_componentes_por_coluna = 9

# Instancie os componentes dinamicamente
componentes = []
for i, dados in enumerate(dados_componentes):
    coluna = i % max_componentes_por_coluna
    linha = i // max_componentes_por_coluna * 2
    componente = Componente(janela, dados["texto"], dados["imagem_path"], row=linha, column=coluna)
    componentes.append(componente)

# Adicione o botão "Obter Dados" e o combobox na última linha e última coluna
#botao = ttk.Button(janela, text="printdata", command=lambda: print(obter_estado_checkboxes())) #opcao para printar no console
botao = ttk.Button(janela, text="Copy to Clip", command=lambda: copyToClip()) #opcao para copiar para a clipboard
botao.grid(row=11, column=8, columnspan=max_componentes_por_coluna, pady=0,padx=15)

#botão que marca se vai ser adicionado ao registro ou não
goToRegister = tk.BooleanVar()
goToRegister.set(set_register_on_lauch)
registerCheck = ttk.Checkbutton(janela, variable=goToRegister, style='TRadiobutton', text='R')
registerCheck.grid(row=11, column=8, columnspan=max_componentes_por_coluna, pady=0,padx=20,sticky="w")

#adiciona botão para resetar coleta
botao2 = ttk.Button(janela, text="Resetar Marcas", command=lambda: premarcacao_checkbox())
botao2.grid(row=12, column=8, columnspan=max_componentes_por_coluna, pady=0,padx=0)

#campo de texto APPNUM
labelNum = ttk.Label(text="NúmeroApp:")
labelNum.grid(row=11, column=6, columnspan=max_componentes_por_coluna, pady=0,padx=0,sticky="w")
appNum = ttk.Entry(janela, text="0")
appNum.grid(row=11, column=6, columnspan=max_componentes_por_coluna, pady=0,padx=75,sticky="w")

#adiciona imagem arcoiris
imageTK = tk.PhotoImage(file='imagensPrograma\\imagem_lgbt.png')
imgLGBT = ttk.Label(image=imageTK, compound=tk.TOP)
imgLGBT.grid(row=12, column=7, columnspan=max_componentes_por_coluna, pady=0,padx=0,sticky="w")
#falta arrumar isso aqui

#adiciona botão para aumentar appnum
botaoAu = ttk.Button(janela, text="+", command=lambda: changeAppNum(True))
botaoAu.grid(row=12, column=6, columnspan=max_componentes_por_coluna, pady=0,padx=90,sticky="w")

#adiciona botão para diminuir appnum
botaoDi = ttk.Button(janela, text="-", command=lambda: changeAppNum(False))
botaoDi.grid(row=12, column=6, columnspan=max_componentes_por_coluna, pady=0,padx=0,sticky="w")

opcoes_combobox = ["Não avaliado","Vermelho","Laranja","Amarelo","Verde","Azul","Indigo","Violeta","Preto"]
combobox = ttk.Combobox(janela, values=opcoes_combobox)
combobox.grid(row=11, column=7, columnspan=max_componentes_por_coluna, pady=0,padx=15,sticky="w")
combobox.current(0)  # Defina a opção inicial

# Configuração da grade para expandir os componentes
for i in range(max_componentes_por_coluna):
    janela.grid_columnconfigure(i, weight=1)
    janela.grid_rowconfigure(i, weight=1,minsize=0)

def copyToClip():
    estados = 'True\t' + obter_estado_checkboxes()
    
    pyperclip.copy(estados)
    print("Dado copiado para a clipboard")
    if goToRegister.get() : gravar_em_registro(estados)
    criar_pasta()

#aumenta ou diminui o valor inteiro no campo appnumber
def changeAppNum (aumenta):
    a = int(appNum.get())
    if aumenta : 
        a =  a + 1
    else :
        a =  a - 1
    #print(a)
    appNum.delete(0, tk.END)
    appNum.insert(0, a)
          
#cria pasta se tiver um número inteiro no campo appnumber
def criar_pasta():
    temp = 0
    try:
        temp = int(appNum.get()) #pega e transforma em int o número do textField appNum
        nome_pasta = str(temp)
        
        if nome_pasta and diretorio_screenshots:
            caminho_pasta = os.path.join(diretorio_screenshots, nome_pasta)

            try:
                os.makedirs(caminho_pasta)
                print(f'Pasta "{nome_pasta}" criada em "{diretorio_screenshots}"\n')
                appNum.delete(0, tk.END) #deleta o número do textField appNum
                appNum.insert(0, temp+1) #incrementa o número do textField appNum
            except FileExistsError:
                print(f'A pasta "{nome_pasta}" já existe em "{diretorio_screenshots}"\n')
            except Exception as e:
                print(f'Ocorreu um erro ao criar a pasta: {e}')
        else:
            print("Nome de pasta inválido")
    except ValueError:
        #print("Criação de pasta desabilitada")
        print("")

def gravar_em_registro(estados_checkbox):
    # Obter a data e hora atual
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Criar a string que pega o número do aplicativo atual, a data e hora atual e os estados
    linha = f"{str(appNum.get())}/{data_hora_atual}: {estados_checkbox}\n" 

    # Nome do arquivo
    nome_arquivo = diretorio_registro + "registro.txt"

    # Verificar se o arquivo existe, se não, criá-lo
    if not os.path.isfile(nome_arquivo):
        print("Arquivo de registro criado")
        with open(nome_arquivo, "w"):
            pass

    # Abrir o arquivo em modo de adição e gravar a linha
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(linha)
    
    print("Dados gravados em registro")


#seta os componentes da forma correta 
def premarcacao_checkbox():
    i = 0
    combobox.current(0)
    for componente in componentes:
            componente.checkbox_var.set(False)
            if pre_select_features : 
                if i == 0 : componente.checkbox_var.set(True) # Marcando o componente Common Button
                if i == 1 : componente.checkbox_var.set(True) # Marcando o componente Icon Button
                if i == 2 : componente.checkbox_var.set(True) # Marcando o componente Text View
                if i == 3 : componente.checkbox_var.set(True) # Marcando o componente ImageView
                #if i == 1 : componente.checkbox_var.set(True) # Marcando o componente 
                i = i + 1

def obter_estado_checkboxes():
    estados = [componente.checkbox_var.get() for componente in componentes]
    opcao_combobox = combobox.get()
    premarcacao_checkbox()
    return f"{'\t'.join(map(str, estados))}\t{opcao_combobox}"

premarcacao_checkbox()
# Inicie o loop principal
janela.mainloop()
