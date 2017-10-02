# importando  a GUI
from tkinter import *
import clipboard
import os
#widget1 = Frame() #criando o primeiro top level widget e atribuindo o master widget para el
msg = ''
# Criando a GUI variavel
app = Tk()

#Variáevis
arquivo = open('Connections.txt', "r", encoding="utf8")
fin = '' #Frase a ser exibida
resto = int(0) #Recebe o resto
a = []
f = ':'
temp = 0
temp2 = ' '
hora = 0
loged = ''
lseg = 0
duracao = ''
x = 0
durationlist = []
contlist = 0
z = 0
y = 1
dici = {}
LabelDoTempo=StringVar()
LabelDoTempo.set(" ")
radiobut = StringVar()
radiobut.set(" ")
linhas = 0
colunas = 0
acumuladorseg = 0
segundosacumulados = 0
tempoacumulado = ''
gaveta = None
selfinho = 0
ID = 0
#class App:
 #   def __init__(self, master):
  #      self.frame= Frame(master)
   #     self.frame.pack(side = BOTTOM)
        
    #    return
def imprime(self):
        z = Radiobutton(text = fin, variable = radiobut, value =duracao, bg='lightyellow' )
        z['font'] = ('Calibri', '10')
        z['width'] = 55
        z.pack(side = TOP)
        durationlist.append(duracao)
        return

def copyvalueedit():
    clipboard.copy(radiobut.get())
    return
def copyvalue():
    a = (durationlist[len(durationlist)-1])
    clipboard.copy(a)
def xrec():
    x = 1
    if x == 1:
        arquivo = open ('Connections.txt', 'w')
        arquivo.close()
        code()
def code(): #Função do Refresh
    os.startfile('init.bat')


'''
def conversor(): # Função bem doida pra converter o tempo seg -> hh:mm:ss
    global acumuladorseg
    global tempoacumulado
    global gaveta
    #global LabelDoTempo
    gaveta=acumuladorseg
    hora = acumuladorseg/3600
    hora = int(hora)
    acumuladorseg= acumuladorseg - int(hora*3600)
    minutos=acumuladorseg/60
    minutos = int(minutos)
    acumuladorseg=acumuladorseg-(minutos*60)
    seg= abs(acumuladorseg)
    if len(str(hora))!=2:
        hora = "0"+str(hora)
    if len(str(minutos))!=2:
        minutos = "0"+str(minutos)
    if len(str(seg))!=2:
        seg = "0"+str(seg)
    tempoacumulado = str(hora)+':'+str((minutos))+':'+str((seg))
    
    return (str(tempoacumulado))
'''
def UpdateLabelDoTempo(self): #Função para atualizar a Label de tempo acumulado
    #global tempoacumulado
    LabelDoTempo.set(self)
    return

def zera():
    UpdateLabelDoTempo(" ")
    
def copyacumulado(): #Função que copia o valor acumulado (e converte o tempo)
    #a = conversor()
    global teste
    clipboard.copy(teste)
teste = None
def conversorlabel(self):
    global selfinho
    global teste
    interno = selfinho + self
    hora = interno/3600
    hora = int(hora)
    interno = interno - int(hora*3600)
    minutos = interno/60
    minutos = int(minutos)
    interno = interno - (minutos*60)
    seg = abs(interno)
    if len(str(hora))!=2:
        hora = "0"+str(hora)
    if len(str(minutos))!=2:
        minutos = "0"+str(minutos)
    if len(str(seg))!=2:
        seg = "0"+str(seg)
    teste = str(hora)+':'+str((minutos))+':'+str((seg))
    return (str(hora)+':'+str((minutos))+':'+str((seg)))

def acumula(): #Função Acumuladora dos tempos
    global tempoacumulado
    global acumuladorseg
   # global LabelDoTempo
    if (radiobut.get())!= ' ':
        a = radiobut.get()
        
        hr,mn,sg=a.split(':')
        #updateLabelDoTempo()
        
        acumuladorseg = int(acumuladorseg)+(int(hr)*3600)+(int(mn)*60)+int(sg)
        UpdateLabelDoTempo(conversorlabel(acumuladorseg))
copyacumulado()
#aplicação(app)

#title
#subtl = Label(text="Log TeamViewer")
#subtl["width"] = 60
#subtl.config(bg="lightblue")
#subtl['font']=('Calibri','15','bold')
#subtl.pack()
class App:
    def __init__(self, master):
        #Definindo containers
        self.frame= Frame(master, bg='lightblue')
        self.frame.pack()
        self.frame2 = Frame(master)
        self.frame2.pack(side=RIGHT)
        self.frame3 = Frame(master)
        self.frame3.pack(side=LEFT)
        
        #Tratando a Janela
        self.titulo = Label(self.frame, text="Log TeamViewer")
        self.titulo["width"] = 60
        self.titulo.config(bg="lightblue")
        self.titulo['font']=('Calibri','15','bold')
        self.titulo.pack(side=TOP)

        #Botão de Apagar o Acumulado
        self.labelo = Button(self.frame2, text="Zera Acumulado", command = zera, width = 21, bg='ivory')
        self.labelo.pack(side=TOP)
        #Label Do Tempo Acumulado
        self.labela = Label(self.frame2,text="a",textvariable=LabelDoTempo)
        self.labela.pack(side= BOTTOM)
        #Botão Acumulador
        self.acumulador= Button(self.frame3, text = "Acumula Valor Selecionado" , command= acumula, width = 21, bg='ivory')
        self.acumulador.pack(side= TOP)

        #Botão De Copiar o Total
        copyacumulador = Button(self.frame3, text= "Copia Total Acumulado", command=copyacumulado, width = 21, bg='ivory')
        copyacumulador.pack(side=BOTTOM)

        

    


App(app)
app.iconbitmap('tumb.ico')
app.config(bg="lightblue")
app.title("ConectionsPy Release 1.0")

for i in arquivo:
            a.append(i)
arquivo.close()
temp3 = len(a)
for cont in range(len(a)):
        temp = a[cont].find(f)
        temp2 = a[cont]
        if temp != -1:
            # Armazena os dois tempos
            n1 = temp2[temp-2:temp+6]
            n2 = temp2[temp+30:temp+38]

            # Separa os valores (hr/mn/seg)
            a1, a2, a3 = n1.split(':')
            a1 = int(a1)
            a2 = int(a2)
            a3 = int(a3)
            b1, b2, b3 = n2.split(':')
            b1 = int(b1)
            b2 = int(b2)
            b3 = int(b3)
            
            #calcula data e hora
            sega = (a1*3600)+(a2*60)+(a3) #Calcula o tempo 1 em segundos
            segb = (b1*3600)+(b2*60)+(b3) #Calcula o tempo 2 em segundos
            #lseg = b3 - a3
            #lseg = abs(lseg)
            seg = segb - sega 
            hora = int(seg/3600) # Calcula as horas
            seg = seg - (hora*3600)
            #minutos = (seg -(3600*hora))/60 # Calcula os minutos
            minutos = (seg)/60
            seg = seg - (minutos*60)
            lseg =abs(sega-segb) - abs((int(hora)*3600)+(int(minutos)*60)) # Calcula os segundos
    
            temp3 -= 1
            data = temp2[temp-2:temp+6]
            d1, d2, d3 = data.split(':')
            d1 = int(d1) - 3
            if len(str(d1))<2:
                d1 = "0"+str(d1)
            data = str(d1)+':'+d2+':'+d3
            minutos = int(minutos)
            #Corrige as casas decimais
            if len(str(hora))<2:
                hora = "0"+str(hora)
            if len(str(minutos))<2:
                minutos = "0"+str(minutos)
            if len(str(lseg))<2:
                lseg = "0"+str(lseg)
            duracao = str(hora)+':'+str(minutos)+':'+str(lseg) #concatena tudo pra uma variavel só
            ID = int(temp2[0:9]) 
            fin = ('%dº Acesso' %temp3, 'Id: %d'%ID,' Inicio: %sh' %data, ' Duração: %s' %duracao)
            fin = fin
            dici[temp3] = [duracao]
            imprime(fin)
            contlist = contlist + 1


#Botão de Refresh o programa
refresh = Button(master = app, text = "Refresh", command = code)
refresh.pack(side = LEFT, anchor = NE,  pady = 10)

#Botão que apaga e depois ativa o Refresh
apaga = Button(master = app, text = "Apagar", command = xrec)
apaga.pack(side = LEFT, anchor = NE,  padx = 10, pady = 10)



        
#Botões de cópia que irão surgir se houver linhas no arquivo
if len(durationlist)>0:            
    coopy = Button(master=app, text = "Copiar Ultima Duração " , command=copyvalue)
    coopy.pack(side = RIGHT, anchor = SE, pady = 10)
if len(durationlist)>0:            
    copy = Button(master=app, text = "Copiar Selecionado" , command=copyvalueedit)
    copy['width']= 14
    copy.pack(side = RIGHT, anchor =SE, padx= 10, pady = 10)
#if len(durationlist)>0:
#    acumulador= Button(master=app, text = "Acumula Valor Selecionado" , command= acumula)
#    acumulador.pack(side= LEFT)
#if len(durationlist)>0:
#    copyacumulador = Button(master=app, text= "Copia Total Acumulado", command=copyacumulado)
#    copyacumulador.pack(side=LEFT)
#if len(durationlist)>0:
#    labela = Label(master=app, textvariable=LabelDoTempo)
#    labela.pack(side=RIGHT, padx = 50)
#if len(durationlist)>0:
#    labelo = Button(master=app, text="Zera Acumulado", command = zera)
#    labelo.pack(side=LEFT)

       
app.mainloop()



    


