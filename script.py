import os
from tkinter import *
from tkinter.filedialog import askdirectory#https://www.tutorialspoint.com/python/python_gui_programming.htm

bgColor = '#75bbfd'
fgColor = '#000000'

window = Tk()
window.configure(background=bgColor, height=450, width=800)

def crarComponente():
    if (direccion.get() == "Elegir Carpeta" or nombre.get() == "" or tipo.get() == "Elegir tipo"):
        print('llenar campos')
        l5.place(x=280,y=350)
    else:
        #cambiar dir
        os.chdir(direccion.get())
        #correr nrcg
        cmdNRCG = 'nrcg -n ' + nombre.get()
        os.system(cmdNRCG)
        print('success', direccion.get(), nombre.get(), tipo.get())
        l5.place_forget()

        #cambiar a pantalla


def elegirDireccion():
    global direccion
    path = askdirectory(title='Elegir Carpeta') # shows dialog box and return the path
    direccion.set(path)


l1 = Label(window, text="Creador de Componentes React", bg=bgColor, fg=fgColor)
l1.config(font=('',20))
l1.place(x=200,y=30)

l2 = Label(window, text="Dirección del componente", bg=bgColor, fg=fgColor)
l2.config(font=('',16))
l2.place(x=140,y=100)
direccion = StringVar()
direccion.set('Elegir Carpeta')
e1=Button(window, command=elegirDireccion, textvariable=direccion, width=20)
e1.config(font=('',16))
e1.place(x=400,y=100)


l3 = Label(window, text="Nombre del componente", bg=bgColor, fg=fgColor)
l3.config(font=('',16))
l3.place(x=140,y=150)
nombre = StringVar()
e2=Entry(window, textvariable=nombre)
e2.config(font=('',16))
e2.place(x=400,y=150)



l4 = Label(window, text="Tipo del componente", bg=bgColor, fg=fgColor)
l4.config(font=('',16))
l4.place(x=140,y=200)
# e2_value = StringVar()
# e2=Entry(window, textvariable=e1_value)
# e2.config(font=('',16))
# e2.place(x=400,y=140)
tipos = ['Funcional', 'De Clase', 'Con Redux']
tipo = StringVar(window)
tipo.set('Elegir tipo')
om1 = OptionMenu(window, tipo, *tipos)
om1.config(font=('',16))
om1.place(x=400,y=200)

b1 = Button(window, text="Crear Componente", command=crarComponente,width=15, bg='#d9ecff', fg=fgColor)
b1.config(font=('',16))
b1.place(x=300,y=300)

l5 = Label(window, text="Llenar todos los campos", bg=bgColor, fg='red')
l5.config(font=('',16))

window.mainloop()
