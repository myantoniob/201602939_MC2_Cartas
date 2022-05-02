
from tkinter import *
from turtle import width




root = Tk()
root.geometry("930x600")
root.resizable(width=False, height=False)

#   --------------------------------------

main_label = LabelFrame(root, width=930, height=600)
main_label.grid_propagate(0)
main_label.grid(row=0, column=0)

#   --------------------------------------

label_get_cartas = Label(main_label, text='Cartas por Jugar')
label_get_cartas.place(x=100, y=25)

opsion_get_cartas = StringVar()
opsion_get_cartas.set("  #Cartas  ")
opsiones = [9,21,27,33,39,45,51,57,63,69,75,81]
drop_menu_cartas = OptionMenu(main_label, opsion_get_cartas,*opsiones)
drop_menu_cartas.place(x=200, y=25)

#   ---------------------------------------

cantidad_cartas = 9
cartas1 = []
cartas2 = []
cartas3 = []

lista_uno = []
lista_dos = []
lista_tres = []
lista_numeros = []

color_uno = []
color_dos = []
color_tres = []
lista_colores = []

cartas_total = []

seleccion = 0

   

def reset_carta(carta):
    carta.destroy() 

def reset_frame(cartas_grupo):
     

    for i in range(cartas_grupo):
        try:
            aux = cartas1.pop()
            aux.destroy() 
        except:
            pass 

    for i in range(cartas_grupo):
        try:
            aux = cartas2.pop()
            aux.destroy()
        except:
            pass 

    for i in range(cartas_grupo):
        try:
            aux = cartas3.pop()
            aux.destroy()
        except:
            pass 
    
    button_uno.pack_forget()
    button_dos.pack_forget()
    button_tres.pack_forget()



def revolver1():
    # LabelFrame(main_label, width=100, height=150, background="green", text=cartas_grupo*2 + i + 1)

    for i in range(len(lista_dos)):
        lista_numeros.append(lista_dos.pop(0))
        lista_colores.append(color_dos.pop(0)) 

    for i in range(len(lista_uno)):
        lista_numeros.append(lista_uno.pop(0))
        lista_colores.append(color_uno.pop(0))

    for i in range(len(lista_tres)):
        lista_numeros.append(lista_tres.pop(0))
        lista_colores.append(color_tres.pop(0)) 

    cartas_grupo = int(len(lista_numeros) / 3)
    

    for i in range(cartas_grupo):
        lista_uno.append(lista_numeros.pop(0))
        lista_dos.append(lista_numeros.pop(0))
        lista_tres.append(lista_numeros.pop(0))

        color_uno.append(lista_colores.pop(0))
        color_dos.append(lista_colores.pop(0))
        color_tres.append(lista_colores.pop(0))
    
    reset_frame(cartas_grupo)


    for i in range(cartas_grupo):
        cartas1.append(LabelFrame(main_label, width=100, height=150, background=f"{color_uno[i]}", text=lista_uno[i]))
        cartas1[i].place(x=30+(i*10), y=100+(i*10))
        position = i

    button_uno.place(x=30+(position*10), y=(position*10)+260)

    for i in range(cartas_grupo):
        cartas2.append(LabelFrame(main_label, width=100, height=150, background=f"{color_dos[i]}", text=lista_dos[i]))
        cartas2[i].place(x=290+(i*10), y=100+(i*10))
        position = i

    #button_dos = Button(main_label, text="  Grupo 2   ")
    button_dos.place(x=290+(i*10), y=(i*10)+260)


    for i in range(cartas_grupo):
        cartas3.append(LabelFrame(main_label, width=100, height=150, background=f"{color_tres[i]}", text=lista_tres[i]))
        cartas3[i].place(x=550+(i*10), y=100+(i*10))
        position = i 

    #button_tres = Button(main_label, text=" Grupo 3 ")
    button_tres.place(x=550+(position*10), y=(position*10)+260)

    n = int((len(lista_dos)  + 1) /2)
    #print(lista_dos[n-1])

    carta_elegida = Label(main_label, text=f'Carta Eligida # {lista_dos[n-1]}')
    carta_elegida.place(x=550, y=25)

    

def revolver2():
    for i in range(len(lista_uno)):
        lista_numeros.append(lista_uno.pop(0))
        lista_colores.append(color_uno.pop(0)) 

    for i in range(len(lista_dos)):
        lista_numeros.append(lista_dos.pop(0))
        lista_colores.append(color_dos.pop(0))

    for i in range(len(lista_tres)):
        lista_numeros.append(lista_tres.pop(0))
        lista_colores.append(color_tres.pop(0)) 

    cartas_grupo = int(len(lista_numeros) / 3)

    
    
    for i in range(cartas_grupo):
        lista_uno.append(lista_numeros.pop(0))
        lista_dos.append(lista_numeros.pop(0))
        lista_tres.append(lista_numeros.pop(0))

        color_uno.append(lista_colores.pop(0))
        color_dos.append(lista_colores.pop(0))
        color_tres.append(lista_colores.pop(0))
    
    reset_frame(cartas_grupo)


    for i in range(cartas_grupo):
        cartas1.append(LabelFrame(main_label, width=100, height=150, background=f"{color_uno[i]}", text=lista_uno[i]))
        cartas1[i].place(x=30+(i*10), y=100+(i*10))
        position = i

    button_uno.place(x=30+(position*10), y=(position*10)+260)

    for i in range(cartas_grupo):
        cartas2.append(LabelFrame(main_label, width=100, height=150, background=f"{color_dos[i]}", text=lista_dos[i]))
        cartas2[i].place(x=290+(i*10), y=100+(i*10))
        position = i

    #button_dos = Button(main_label, text="  Grupo 2   ")
    button_dos.place(x=290+(i*10), y=(i*10)+260)


    for i in range(cartas_grupo):
        cartas3.append(LabelFrame(main_label, width=100, height=150, background=f"{color_tres[i]}", text=lista_tres[i]))
        cartas3[i].place(x=550+(i*10), y=100+(i*10))
        position = i 

    #button_tres = Button(main_label, text=" Grupo 3 ")
    button_tres.place(x=550+(position*10), y=(position*10)+260)

    n = int((len(lista_dos)  + 1) /2)
    #print(lista_dos[n-1])

    carta_elegida = Label(main_label, text=f'Carta Eligida # {lista_dos[n-1]}')
    carta_elegida.place(x=550, y=25)


def revolver3():
    for i in range(len(lista_uno)):
        lista_numeros.append(lista_uno.pop(0))
        lista_colores.append(color_uno.pop(0)) 

    for i in range(len(lista_tres)):
        lista_numeros.append(lista_tres.pop(0))
        lista_colores.append(color_tres.pop(0))

    for i in range(len(lista_dos)):
        lista_numeros.append(lista_dos.pop(0))
        lista_colores.append(color_dos.pop(0)) 

    cartas_grupo = int(len(lista_numeros) / 3)

    
    for i in range(cartas_grupo):
        lista_uno.append(lista_numeros.pop(0))
        lista_dos.append(lista_numeros.pop(0))
        lista_tres.append(lista_numeros.pop(0))

        color_uno.append(lista_colores.pop(0))
        color_dos.append(lista_colores.pop(0))
        color_tres.append(lista_colores.pop(0))
    
    reset_frame(cartas_grupo)


    for i in range(cartas_grupo):
        cartas1.append(LabelFrame(main_label, width=100, height=150, background=f"{color_uno[i]}", text=lista_uno[i]))
        cartas1[i].place(x=30+(i*10), y=100+(i*10))
        position = i

    button_uno.place(x=30+(position*10), y=(position*10)+260)

    for i in range(cartas_grupo):
        cartas2.append(LabelFrame(main_label, width=100, height=150, background=f"{color_dos[i]}", text=lista_dos[i]))
        cartas2[i].place(x=290+(i*10), y=100+(i*10))
        position = i

    #button_dos = Button(main_label, text="  Grupo 2   ")
    button_dos.place(x=290+(i*10), y=(i*10)+260)


    for i in range(cartas_grupo):
        cartas3.append(LabelFrame(main_label, width=100, height=150, background=f"{color_tres[i]}", text=lista_tres[i]))
        cartas3[i].place(x=550+(i*10), y=100+(i*10))
        position = i 

    #button_tres = Button(main_label, text=" Grupo 3 ")
    button_tres.place(x=550+(position*10), y=(position*10)+260)

    n = int((len(lista_dos)  + 1) /2)
    #print(lista_dos[n-1])

    
    carta_elegida = Label(main_label, text=f'Carta Eligida # {lista_dos[n-1]}')
    carta_elegida.place(x=550, y=25)




button_uno = Button(main_label, text="  Grupo 1 ", command = revolver1)
button_dos = Button(main_label, text="  Grupo 2   ", command = revolver2)
button_tres = Button(main_label, text=" Grupo 3 ", command = revolver3)

#def onclick(event):
#    event.widget.config(bg='yellow')


def iniciar():
    position = 0
    
    cantidad_cartas = 0
    try:
        cantidad_cartas =  int(opsion_get_cartas.get())
    except:
        pass 
    cartas_grupo = int(cantidad_cartas / 3)

    label_confirmacion_cartas = Label(main_label, text=f'Juagras con #{cantidad_cartas} de Cartas')
    label_confirmacion_cartas.place(x=400, y=25)
    
    if len(cartas1) != 0:
        reset_frame(len(cartas1))

    for i in range(cartas_grupo):
        cartas1.append(LabelFrame(main_label, width=100, height=150, background="red", text=i + 1))
        lista_uno.append(i+1)
        color_uno.append('red')
        cartas1[i].place(x=30+(i*10), y=100+(i*10))
        position = i

    button_uno.place(x=30+(position*10), y=(position*10)+260)

    for i in range(cartas_grupo):
        cartas2.append(LabelFrame(main_label, width=100, height=150, background="blue", text=cartas_grupo + i + 1))
        lista_dos.append(cartas_grupo + i + 1)
        color_dos.append('blue')
        cartas2[i].place(x=290+(i*10), y=100+(i*10))
        position = i

    #button_dos = Button(main_label, text="  Grupo 2   ")
    button_dos.place(x=290+(i*10), y=(i*10)+260)


    for i in range(cartas_grupo):
        cartas3.append(LabelFrame(main_label, width=100, height=150, background="green", text=cartas_grupo*2 + i + 1))
        lista_tres.append(cartas_grupo*2 + i + 1)
        color_tres.append('green')
        cartas3[i].place(x=550+(i*10), y=100+(i*10))
        position = i 

    #button_tres = Button(main_label, text=" Grupo 3 ")
    button_tres.place(x=550+(position*10), y=(position*10)+260)
        
#   -------------------------------
button_set_cartas = Button(main_label, text="Empesar", command= iniciar)
button_set_cartas.place(x=300, y=25)





root.mainloop()