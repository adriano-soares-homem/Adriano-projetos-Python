from tkinter import *
import random
import string

lista_caracteresp = ['!', '@', "#",'$','%','&','*']
lista_senha = []    
telaprin = Tk()
telaprin.geometry("800x500")
telaprin.title('Gerador de senha')
telaprin.iconphoto(False, PhotoImage(file='Cadeado.ico'))
quant = 0
botao = IntVar()
botao2 = IntVar()
botao3 = IntVar()
botao4 = IntVar()

def AClicado():
    lista_senha.clear()
    global quant
    quant = int(senha.get('1.0','end-1c'))
    
    num_caracteres = 0
    
    while num_caracteres <= quant:
        if botao.get() == 1:  
            lista_senha.append(chr(random.randint(ord("A"), ord("Z"))))
            num_caracteres += 1
        if num_caracteres == quant:
                break
        if botao2.get() == 1:  
            lista_senha.append(chr(random.randint(ord("a"), ord("z"))))
            num_caracteres += 1            
        if num_caracteres == quant:
                break
        if botao3.get() == 1:  
            lista_senha.append(random.choice(lista_caracteresp))
            num_caracteres += 1  
        if num_caracteres == quant:
                break
        if botao4.get() == 1:  
            lista_senha.append(str(random.randint(1, 9)))
            num_caracteres += 1  
        if num_caracteres == quant:
                break
       

def Continuar():
    global lista_senha
    AClicado()  
    senha_gerada = ''.join(lista_senha)
    senhagerada.config(text=senha_gerada)

def Copiar():
     telaprin.clipboard_clear()
     senha_gerada = senhagerada.cget("text")
     telaprin.clipboard_append(senha_gerada)


msg = Label(telaprin, text='Digite a quantide de caracteres você quer', height=1,)
bot1 = Checkbutton(telaprin, text= 'A-Z', variable= botao, onvalue = 1, offvalue = 0, height=1,width = 5,)
bot2 = Checkbutton(telaprin, text='a-z', variable=botao2, onvalue=1, offvalue=0, height=1, width= 5,)
bot3 = Checkbutton(telaprin, text='!@#$%&*', variable=botao3, onvalue=1, offvalue=0, height=1, width=7,)
bot4 = Checkbutton(telaprin, text='1-9', variable=botao4, onvalue=1, offvalue=0, height=1, width=6,)
senha = Text(telaprin, height=1, width=10)
finalizar = Button(telaprin, text='Finalizar', command=Continuar)
senhagerada = Label(telaprin, text='', height=1, font=('Arial', 25))
copiar = Button(telaprin, height=1, width=5, text="Copiar", command=Copiar)
msg.place(x=305, y=10)
senha.place(x=370, y=30)
bot1.place(x=290, y=50)
bot2.place(x=340, y=50)
bot3.place(x=400, y=50)
bot4.place(x=475, y=50)
senhagerada.place(x=320, y=200)
finalizar.place(x=380, y=300)
copiar.place(x=384, y=327)





telaprin.mainloop()

