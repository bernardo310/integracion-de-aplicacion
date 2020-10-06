import os
from tkinter import *
from tkinter.filedialog import askdirectory#https://www.tutorialspoint.com/python/python_gui_programming.htm

bgColor = '#ffffff'
fgColor = '#000000'

window = Tk()
window.configure(background=bgColor, height=400, width=800)

#Funcion para crear el comando
def crearComponente():
    #Revisa si se llenaron los campos obligatorios
    if (direccion.get() == "Elegir Carpeta" or nombre.get() == ""):
        print('llenar campos')
        l5.place(x=280,y=350)
    else:
        #cambiar dir
        os.chdir(direccion.get())
        #Empieza a crear el string del comando
        cmdNRCG = 'nrcg -n ' + nombre.get() + ' '
        #Agrega las opciones al string
        if (var_r.get() == 1):
            cmdNRCG += '-r '
        if (var_v.get() == 1):
            cmdNRCG += '-v '
        if (var_c.get() == 1):
            cmdNRCG += '-c '
        if (var_s.get() == 1):
            cmdNRCG += '-s '
        #Corre el comando
        os.system(cmdNRCG)
        print(cmdNRCG)
        l5.place_forget()

        #cambiar a pantalla

#Funcion para elegir carpeta
def elegirDireccion():
    global direccion
    path = askdirectory(title='Seleccionar direccion') # shows dialog box and return the path
    direccion.set(path)

#Titulo
l1 = Label(window, text="Creador de Componentes React", bg=bgColor, fg=fgColor, font='Helvetica 20 bold')
l1.place(x=230, y=30)

#Selección de direccion
l2 = Label(window, text="Dirección del componente", bg=bgColor, fg=fgColor)
l2.config(font='Helvetica 16 bold')
l2.place(x=140,y=100)
direccion = StringVar()
direccion.set('Seleccionar carpeta')
e1=Button(window, command=elegirDireccion, textvariable=direccion, width=20)
e1.config(font='Helvetica 16')
e1.place(x=400,y=100)

#Nombre del componente
l3 = Label(window, text="Nombre del componente", bg=bgColor, fg=fgColor)
l3.config(font='Helvetica 16 bold')
l3.place(x=140,y=150)
nombre = StringVar()
e2=Entry(window, textvariable=nombre)
e2.config(font=('',16))
e2.place(x=400,y=150)

#Checkbox de opciones
l4 = Label(window, text="Opciones a añadir", bg=bgColor, fg=fgColor)
l4.config(font='Helvetica 16 bold')
l4.place(x=140,y=237.5)
# e2_value = StringVar()
# e2=Entry(window, textvariable=e1_value)
# e2.config(font=('',16))
# e2.place(x=400,y=140)
tipos = ['Redux', 'React Arrow', 'CSS', 'Node sass']
var_r = IntVar(window)
var_v = IntVar(window)
var_c = IntVar(window)
var_s = IntVar(window)
var_r.set('Elegir opciones')
opcion1 = Checkbutton(window, text=tipos[0], variable=var_r, onvalue = 1, offvalue = 0)
opcion1.config(font=('', 16))
opcion1.place(x=400,y=200)
opcion2 = Checkbutton(window, text=tipos[1], variable=var_v, onvalue = 1, offvalue = 0)
opcion2.config(font=('', 16))
opcion2.place(x=400, y=225)
opcion3 = Checkbutton(window, text=tipos[2], variable=var_c, onvalue = 1, offvalue = 0)
opcion3.config(font=('', 16))
opcion3.place(x=400, y=250)
opcion4 = Checkbutton(window, text=tipos[3], variable=var_s, onvalue = 1, offvalue = 0)
opcion4.config(font=('', 16))
opcion4.place(x=400, y=275)

#Boton de crear
b1 = Button(window, text="Crear componente", command=crearComponente,width=15, bg='#d9ecff', fg=fgColor)
b1.config(font=('',16))
b1.place(x=300,y=325)

#Mensaje de error
l5 = Label(window, text="No todos los campos estan llenos", bg=bgColor, fg='red')
l5.config(font=('',16))

window.mainloop()
