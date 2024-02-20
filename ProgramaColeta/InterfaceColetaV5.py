import tkinter as tk
from tkinter import ttk
import pyperclip
import os
from datetime import datetime

diretorio_screenshots = "Screenshots\\"
diretorio_registro = "registro\\"
set_register_on_lauch = True
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
    {"texto": "Pre-loading indicator", "imagem_path": "visual-representation\\Pre-loading indicator.png"},
    {"texto": "Badge", "imagem_path": "visual-representation\\Badge.png"},
    {"texto": "Snackbar", "imagem_path": "visual-representation\\Snackbar.png"},
    {"texto": "Tool tip", "imagem_path": "visual-representation\\Tool tip.png"},
    {"texto": "Extended FAB", "imagem_path": "visual-representation\\Extended FAB.png"},
    {"texto": "Floating action button", "imagem_path": "visual-representation\\Floating action button.png"},
    {"texto": "Bottom app bar", "imagem_path": "visual-representation\\Bottom app bar.png"},
    {"texto": "Web component", "imagem_path": "visual-representation\\Web component.png"},
    {"texto": "Background music", "imagem_path": "visual-representation\\Background music.png"},
    {"texto": "Date picker", "imagem_path": "visual-representation\\Date picker.png"},
    {"texto": "Dial time picker", "imagem_path": "visual-representation\\Dial time picker.png"},
    {"texto": "Digital time picker ", "imagem_path": "visual-representation\\Digital time picker.png"},
    {"texto": "Radio button", "imagem_path": "visual-representation\\Radio button.png"},
    {"texto": "Switch", "imagem_path": "visual-representation\\Switch.png"},
    {"texto": "Checkbox", "imagem_path": "visual-representation\\Checkbox.png"},
    {"texto": "Slider", "imagem_path": "visual-representation\\Slider.png"},
    {"texto": "Map view", "imagem_path": "visual-representation\\Map view.png"},
    {"texto": "Videos", "imagem_path": "visual-representation\\Videos.png"},
    {"texto": "Segmented Buttons", "imagem_path": "visual-representation\\Segmented Buttons.png"},
    {"texto": "Chip", "imagem_path": "visual-representation\\Chip.png"},
    {"texto": "Primary tab", "imagem_path": "visual-representation\\Primary tab.png"},
    {"texto": "Secondary tab", "imagem_path": "visual-representation\\Secondary tab.png"},
    {"texto": "Bottom sheet", "imagem_path": "visual-representation\\Bottom sheet.png"},
    {"texto": "Side sheet", "imagem_path": "visual-representation\\Side sheet.png"},
    {"texto": "Menu", "imagem_path": "visual-representation\\Menu.png"},
    {"texto": "Linear progress indicator", "imagem_path": "visual-representation\\Linear progress indicator.png"},
    {"texto": "Circular progress indicator", "imagem_path": "visual-representation\\Circular progress indicator.png"},
    {"texto": "Account required", "imagem_path": "visual-representation\\Account required.png"},
    {"texto": "Default night mode", "imagem_path": "visual-representation\\Default night mode.png"},
    {"texto": "Landscape mode", "imagem_path": "visual-representation\\Landscape mode.png"},
    {"texto": "Sound Effects", "imagem_path": "visual-representation\\Sound Effects.png"},
    {"texto": "Social interaction", "imagem_path": "visual-representation\\Social interaction.png"},
    {"texto": "Text field", "imagem_path": "visual-representation\\Text field.png"},
    {"texto": "Search", "imagem_path": "visual-representation\\Search.png"},
    {"texto": "Dialog", "imagem_path": "visual-representation\\Dialog.png"},
    {"texto": "Full-screen dialog", "imagem_path": "visual-representation\\Full-screen dialog.png"},
    {"texto": "Navigation rail", "imagem_path": "visual-representation\\Navigation rail.png"},
    {"texto": "Navigation drawer", "imagem_path": "visual-representation\\Navigation drawer.png"},
    {"texto": "Navigation bar", "imagem_path": "visual-representation\\Navigation bar.png"},
    {"texto": "Top app bar", "imagem_path": "visual-representation\\Top app bar.png"},
    {"texto": "Card list", "imagem_path": "visual-representation\\Card list.png"},
    {"texto": "Grid layout", "imagem_path": "visual-representation\\Grid layout.png"},
    {"texto": "Carousel", "imagem_path": "visual-representation\\Carousel.png"},
    {"texto": "Divider", "imagem_path": "visual-representation\\Divider.png"},
    {"texto": "List", "imagem_path": "visual-representation\\List.png"},
    {"texto": "Common button", "imagem_path": "visual-representation\\Common button.png"},
    {"texto": "Icon button", "imagem_path": "visual-representation\\Icon button.png"},
    {"texto": "Text view", "imagem_path": "visual-representation\\Text view.png"},
    {"texto": "Images", "imagem_path": "visual-representation\\Images.png"},

    #pre-marcados  - Line 6




    
    
    
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
imageTK = tk.PhotoImage(file='visual-representation\\image_rainbow.png')
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
    #i = 0
    combobox.current(0)
    for componente in componentes:
            componente.checkbox_var.set(False)

    if pre_select_features :
        componentes[45].checkbox_var.set(True)
        componentes[46].checkbox_var.set(True)
        componentes[47].checkbox_var.set(True)
        componentes[48].checkbox_var.set(True)

def obter_estado_checkboxes():
    estados = [componente.checkbox_var.get() for componente in componentes]
    opcao_combobox = combobox.get()
    premarcacao_checkbox()
    return f"{'\t'.join(map(str, estados))}\t{opcao_combobox}"

premarcacao_checkbox()
# Inicie o loop principal
janela.mainloop()
