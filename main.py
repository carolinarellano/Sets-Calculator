import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

from numpy import append
import functions
from random import randint

set_A = []
set_B = []

def generador_conjuntos():
    def agregar_elemento(entry, conjunto):
        if len(conjunto) == 20:
            errorLabel = tk.Label(frame_main, text="El conjunto llegó al límite de elementos", font="Helvetica 8", fg="red")
            errorLabel.place(x=30, y=350)
        else:
            elemento = entry.get()
            conjunto.append(elemento)
            entry.delete(0,END)

    def agregar_elemento_random(entry, conjunto):
        for i in range(randint(0, 20)):
            conjunto.append(randint(1, 101))
        entry.delete(0,END)
    
    def eliminar_elemento(entry, conjunto):
        conjunto.pop(-1)
        entry.delete(0,END)

    def guardar_conjuntos():
        mostrarconjuntoA = LabelFrame(frame_main, text= "Conjunto A", bg="antique white", font= "Helvetica 8 italic", width=320, height=50)
        cA = Label(mostrarconjuntoA, text= set_A, bg="antique white", font= "Helvetica 8")
        mostrarconjuntoA.place(x=30, y=250)
        cA.place(x=0, y=0)
        mostrarconjuntoB = LabelFrame(frame_main, width=320, height=50, text= "Conjunto B", bg="antique white", font= "Helvetica 8 italic")
        cB = Label(mostrarconjuntoB, text= set_B, bg="antique white", font= "Helvetica 8")
        mostrarconjuntoB.place(x=30, y=300)
        cB.place(x=0, y=0)
        
    def limpiar_conjuntos(conjunto1, conjunto2):
        conjunto1.clear()
        conjunto2.clear()

    frame_main = Frame(window)
    frame_main.place(x=0, y=200)
    frame_main.config(background='antique white', width=400, height=400)
    conjA =Label(frame_main, text= "Conjunto A", font="Helvetica 10 bold", bg='antique white')
    conjA.place(x=90, y=35)
    conjunto_etiqueta = Label(frame_main, text= "Ingresar elemento por elemento", font="Helvetica 8", bg='antique white')
    conjuntoA = Entry(frame_main)
    conjuntoA.config(width=5)
    conjunto_etiqueta.place(x=125, y=20)
    conjuntoA.place(x=110, y=60)
    conjuntoABoton = Button(frame_main, text= "Agregar", font="Helvetica 10", bg='DarkOliveGreen3', 
                            fg='DarkOliveGreen4', relief='groove', command= lambda: agregar_elemento(conjuntoA, set_A))
    conjuntoABoton.place(x=95, y=90)
    conjuntoB = Entry(frame_main)
    conjuntoB.config(width=5)
    conjuntoB.place(x=270, y=60)
    conjB =Label(frame_main, text= "Conjunto B", font="Helvetica 10 bold", bg='antique white')
    conjB.place(x=240, y=35)
    conjuntoBBoton = Button(frame_main, text= "Agregar", font="Helvetica 10", bg='DarkOliveGreen3', 
                            fg='DarkOliveGreen4', relief='groove', command= lambda: agregar_elemento(conjuntoB, set_B))
    conjuntoBBoton.place(x=255, y=90)
    conjuntoA_random = Button(frame_main, text= "RANDOM", font="Helvetica 10", bg='tomato', 
                            fg='white', relief='groove', command= lambda: agregar_elemento_random(conjuntoA, set_A))
    conjuntoA_random.place(x=90, y=160)
    conjuntoB_random = Button(frame_main, text= "RANDOM", font="Helvetica 10", bg='tomato', 
                            fg='white', relief='groove', command= lambda: agregar_elemento_random(conjuntoB, set_B))
    conjuntoB_random.place(x=250, y=160)

    guardarConjuntos = Button(frame_main, text= "Guardar conjuntos", font="Helvetica 9", bg='DarkOliveGreen3', 
                                fg='DarkOliveGreen4', relief='groove', command=lambda: guardar_conjuntos())
    guardarConjuntos.place(x=100, y=200)
    borrarElementoConjuntoA = Button(frame_main, text= "Borrar", font="Helvetica 9", bg='DarkOliveGreen3', 
                                    fg='DarkOliveGreen4', relief='groove', command= lambda: eliminar_elemento(conjuntoA, set_A))
    borrarElementoConjuntoA.place(x=100, y=120)
    borrarElementoConjuntoB = Button(frame_main, text= "Borrar", font="Helvetica 9", bg='DarkOliveGreen3', 
                                    fg='DarkOliveGreen4', relief='groove', command= lambda: eliminar_elemento(conjuntoB, set_B))
    borrarElementoConjuntoB.place(x=260, y=120)
    limpiarConjuntos = Button(frame_main, text= "Limpiar", font="Helvetica 9", bg='DarkOliveGreen3', 
                                fg='DarkOliveGreen4', relief='groove', command= lambda: limpiar_conjuntos(set_A, set_B))
    limpiarConjuntos.place(x=220, y=200)
    

def operadores():
    def mostrar_resultados(operacion, nombre):
        resultados = Toplevel(frame_main)
        resultados.title("Resultados")
        resultados.geometry("500x300")
        resultados.configure(background= "antique white")
        resultado = LabelFrame(resultados, text= "Resultado", bg="antique white", fg= "PaleGreen4", font= "Helvetica 11", width=400, height=200)
        resultado.place(x=50, y=50)
        etiqueta = Label(resultado, text= nombre, bg="antique white", fg= "PaleGreen4", font= "Helvetica 18 bold")
        etiqueta.place(x=70, y=10)
        imprimir = scrolledtext.ScrolledText(resultado, font= "Helvetica 10", fg="tan4", width=30, height=7)
        imprimir.insert(tk.INSERT, operacion) #el texto que vas a colocar
        imprimir.configure(state ='disabled') #para que sea de solo lectura
        imprimir.place(x=70, y=50)


    def acciones(combo):
        if combo.get() == "Intersección":
            interseccion = functions.intersection(set_A, set_B)
            mostrar_resultados(interseccion, combo.get())
        if combo.get() == "Unión":
            union = functions.union(set_A, set_B)
            mostrar_resultados(union, combo.get())
        if combo.get() == "Diferencia A-B":
            diferencia = functions.difference(set_A, set_B)
            mostrar_resultados(diferencia, combo.get())
        if combo.get() == "Diferencia B-A":
            diferencia = functions.difference(set_B, set_A)
            mostrar_resultados(diferencia, combo.get())
        if combo.get() == "Diferencia simétrica":
            simetrica = functions.symmetric_difference(set_A, set_B)
            mostrar_resultados(simetrica, combo.get())
        if combo.get() == "Complemento de A":
            complemento = functions.complement(set_A)
            mostrar_resultados(complemento, combo.get())
        if combo.get() == "Complemento de B":
            complemento = functions.complement(set_B)
            mostrar_resultados(complemento, combo.get())
        if combo.get() == "Producto cartesiano AxB":
            producto = functions.ProductoCartesiano(set_A, set_B)
            mostrar_resultados(producto, combo.get())
        if combo.get() == "Producto cartesiano BxA":
            producto = functions.ProductoCartesiano(set_B, set_A)
            mostrar_resultados(producto, combo.get())
        if combo.get() == "Producto cartesiano AxA":
            producto = functions.ProductoCartesiano(set_A, set_A)
            mostrar_resultados(producto, combo.get())
        if combo.get() == "Producto cartesiano BxB":
            producto = functions.ProductoCartesiano(set_B, set_B)
            mostrar_resultados(producto, combo.get())
        if combo.get() == "Conjunto potencia de A":
            potencia = functions.potencia(set_A)
            mostrar_resultados(potencia, combo.get())
        if combo.get() == "Conjunto potencia de B":
            potencia = functions.potencia(set_B)
            mostrar_resultados(potencia, combo.get())
        if combo.get() == "Cardinalidad de A":
            cardinalidad = functions.Cardinalidad(set_A)
            mostrar_resultados(cardinalidad, combo.get())
        if combo.get() == "Cardinalidad de B":
            cardinalidad = functions.Cardinalidad(set_B)
            mostrar_resultados(cardinalidad, combo.get())
        if combo.get() == "Contención A en B":
            contencion = functions.Contencion(set_A, set_B)
            mostrar_resultados(contencion)
        if combo.get() == "Contención B en A":
            contencion = functions.Contencion(set_B, set_A)
            mostrar_resultados(contencion)
                
    frame_main = Frame(window)
    frame_main.place(x=450, y=200)
    frame_main.config(background='bisque2', width=300, height=300)
    operadores_etiqueta = Label(frame_main, text= "Selecciona la operación que deseas realizar", font="Helvetica 10", bg='bisque2')
    operadores_etiqueta.place(x=20, y=90) 
    lista_operadores = ttk.Combobox(frame_main, values=["(seleccionar)", "Intersección", "Unión", "Diferencia A-B", "Diferencia B-A",
                                                        "Diferencia simétrica", "Complemento de A", "Complemento de B",
                                                        "Producto cartesiano AxB", "Producto cartesiano BxA", "Producto cartesiano AxA", 
                                                        "Producto cartesiano BxB", "Conjunto potencia de A", "Conjunto potencia de B",
                                                        "Cardinalidad de A", "Cardinalidad de B", "Contención A en B", "Contención B en A"])
    lista_operadores.current(0)
    lista_operadores.config(width=35)
    lista_operadores.place(x=50, y=120)
    aceptar_boton = Button(frame_main, text="Aceptar", font="Helvetica 9", bg='DarkOliveGreen3', 
                            fg='DarkOliveGreen4', relief='groove', command=lambda: [acciones(lista_operadores)])                                                
    aceptar_boton.place(x=120, y=150)

window = tk.Tk()
window.title('Conjuntos')
window.geometry('1100x700')
window.config(background="bisque2", padx=100, pady=30)
tittle = tk.Label(text="Conjuntos", fg='PaleGreen4', bg='bisque2', font="Helvetica 30 bold")
descripcion = tk.Label(text="Proyecto de FCC", fg='PaleGreen4', bg='bisque2', font="Helvetica 12")
descripcion.place(x=700, y=50)
tittle.place(x=50, y=50)
nuevo_conjunto = tk.Button(text='Nuevo conjunto', bg='DarkOliveGreen3', font='Helvetica 13 italic', fg='DarkOliveGreen4', relief='groove', command=generador_conjuntos)
nuevo_conjunto.place(x=250, y=150)
operadores = tk.Button(text="Operadores", bg= 'DarkOliveGreen3', font="Helvetica 13 italic", fg='DarkOliveGreen4', relief='groove', command=operadores)
operadores.place(x=450, y=150)
about = tk.Button(text="Acerca de", bg='PaleGreen4', font="Helvetica 13 italic", fg='DarkOliveGreen3', relief='groove')
#about.place(x=800, y= 500)

window.mainloop()