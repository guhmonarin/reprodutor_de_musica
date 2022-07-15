from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from pygame  import mixer, time

musicas=[]

#configurações das cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#2e2d2c"  # black
co4 = "#403d3d"   # letra
co5 = "#4a88e8"  # Azul 

#funcoes do reprodutor

class Reproduzir:
    def __init__(self):
        pass
   
    def escolher():
        #selecionar = askopenfilename(initialdir='C:\Users\gusta\Desktop\programacao\Projetos python\reprodutor_de_musica', filetypes=('arquivos de audio', '*.mp3'), title='selecione as musicas')
        selecionar = open('pray.mp3')
        musicas.append(selecionar)
        return musicas

    def tocar():
        mixer.init()
        mixer.music.load('pray.mp3')
        mixer.music.play()
        mixer.music.set_volume(1)
        
        
        for item in musicas:
            musica_atual=mixer.music.load(item)
            musica_atual=mixer.music.play()

    def parar ():
        musica_atual = mixer.music.stop()

    def pausar ():
        musica_atual = mixer.music.pause()

    def retomar ():
        musica_atual = mixer.music.unpause() 

    def proxima ():
        for item in range(len(musicas)):
            item = 0
            musica_atual = mixer.music.load(musicas[item])  
            musica_atual = mixer.music.play() 

    def anterior ():
        for item in range(len(musicas)):
            item = 0
           # musica_atual = mixer.music.load(musicas[item])
           # musica_atual = mixer.music.play()

    



reproduzir=Reproduzir
#janela principal com as configurações
janela_principal = Tk()
janela_principal.geometry('400x250')
janela_principal.resizable(width=FALSE,height=FALSE)

#configuração do menus
menu=Menu(janela_principal)
inicio=Menu(menu)
inicio.add_command(label='ABRIR', command=reproduzir.escolher())
menu.add_cascade(label="INICIO", menu=inicio)
janela_principal.configure(menu=menu)


#criacao dos frames e suas posições
direita = Frame(janela_principal,width=300, height = 180, bg=co3)
direita.grid(row=0,column=1,pady=1,padx=1,stick=NSEW)

esquerda = Frame(janela_principal,width=180, height = 180,bg=co3)
esquerda.grid(row=0,column=0,pady=1,padx=0,stick=NSEW)

baixo = Frame(janela_principal, width=400, height = 60, bg=co3)
baixo.grid(row=1,column=0, columnspan = 3,pady=1,padx=1,stick=NSEW)

#configuraçoes no frame da esquerda
img_esquerda = Image.open('logo.png')
img_esquerda = img_esquerda.resize((130,130))
img_esquerda = ImageTk.PhotoImage(img_esquerda)

l_logo=Label(esquerda, height=130,image=img_esquerda, compound=LEFT, padx=10, anchor='nw', font=('ivy 16 bold'), bg=co3, fg=co3)
l_logo.place(x=24, y=15)

#configurações no frame da direita
listbox= Listbox(direita, width=30, height=12, selectmode=SINGLE, font=('arial 9 bold'), bg=co3, fg=co3)
listbox.grid(row=0,column=0)

s = Scrollbar(esquerda)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

#configurações no frame debaixo
#play=Button(baixo, text=('ANTERIOR'), command=reproduzir.anterior())
#play.pack()

play=Button(baixo, text=('PLAY'), command=reproduzir.tocar())
play.pack()

pause=Button(baixo, text=('PAUSE'), command=reproduzir.pausar())
pause.pack()

#play=Button(baixo, text=('PROXIMA'), command=reproduzir.proxima())
#play.pack()
    

janela_principal.mainloop()