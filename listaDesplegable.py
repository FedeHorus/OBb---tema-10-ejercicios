from tkinter import *

ventana = Tk()

lista = Listbox(ventana)
for item in ['Autos', 'Motos', 'Barcos', 'Bicicletas', 'Aviones']:
    lista.insert(END, item)

lista.pack()    

etiqueta = Label(ventana, text="Vehiculos",padx= 5, pady=5)    
etiqueta.pack()



ventana.mainloop()
