from tkinter import *

def seleccionar():
    ventana.config(text="{}".format(opcion.get()))  
def reset():
    opcion.set(None)
    ventana.config(text="")
        

inicial = Tk()
opcion= StringVar()
opcion.set(None)

Radiobutton(inicial, text ="Buenos Aires", variable = opcion,
            value = 'Buenos Aires', command=seleccionar).pack(anchor=W)
Radiobutton(inicial, text ="GBA", variable = opcion,
            value = 'GBA', command=seleccionar).pack(anchor=W)
Radiobutton(inicial, text ="Ciudad Autonoma de Buenos Aires", variable = opcion,
            value = 'Ciudad Autonoma de buenos Aires', command=seleccionar).pack(anchor=W)



ventana = Label(inicial)
ventana.pack()
Button(inicial, text ="Reiniciar", command=reset).pack()

ventana.mainloop()
