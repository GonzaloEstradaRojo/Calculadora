from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import math  

raiz=Tk()
raiz.title("Calculadora")
raiz.iconbitmap("D:\Google Drive\Portatil\Programacion\Pildoras informaticas tutoriales\PythonS\graficos\calculadora.ico")
barraMenu=Menu(raiz)
raiz.config(bg="white", menu=barraMenu)

valorNumerico=StringVar()
resultadoPrevioNum=False
numeroOperadores=0
 


calculosLabel = Entry(raiz,  textvariable=valorNumerico)
calculosLabel.grid(row=0,column=0, padx=1, pady=0, sticky="EWNS", columnspan=5)
calculosLabel.config(width=10, justify="cent",font=("Arial Black", 30))
 
#####   Configuracion de la grid para que se autoescale al modificar el tamaño de la venta

raiz.grid_columnconfigure(0, weight=1)
raiz.grid_columnconfigure(1, weight=1)
raiz.grid_columnconfigure(2, weight=1)
raiz.grid_columnconfigure(3, weight=1)
raiz.grid_columnconfigure(4, weight=1)

raiz.grid_rowconfigure(0, weight=1)
raiz.grid_rowconfigure(1, weight=1)
raiz.grid_rowconfigure(2, weight=1)
raiz.grid_rowconfigure(3, weight=1)
raiz.grid_rowconfigure(4, weight=1)


############  FUNCIONES VENTANAS EMERGENTES ERRORES ##########


def divisionCero():

	messagebox.showwarning("Error", "ERROR: ESTAS TRATANDO DE DIVIDIR POR CERO \nMaria Llorente estará riendose de ti allá donde quiera que esté") 


def operacionErronea():
	
	messagebox.showwarning("Error", "Operación no válida. Por favor, revise que las cuentas estan bien")  


############  FUNCIONES MENU ############


def salirAplicacion(): #Preguntas si no. ALmacenan el valor yes or no. Sin sonido

	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

	if valor == "yes":
		raiz.destroy()


def infoAdicional():

	messagebox.showinfo("Calculadora", "Programa hecho en Python por el brillante matemático Gonzalo Estrada siguiendo las directrices del canal de youtube Pildoras informaticas") 


def Ayuda():

	valor = messagebox.askokcancel("Ayuda", "Para desbloquear esta opción debes pagar un total de 26,99€. ¿Estás de acuerdo?") 

	if valor == True:

		messagebox.showinfo("??????", "En serio vas a pagar por la ayuda de esta mierda de programa? Hasta un niño de 10 años entenderíaa como funciona. Deja de vaguear y ponte a tabajar, en vez de estar malgastando el dinero en apliaciones estupidas")  

def Proximamente():

		messagebox.showinfo("Upcoming", "Proximamente en sus mejores ordenadores")



############  BOTONES MENU  ##################


 
opcionesMenu=Menu(barraMenu, tearoff=0)
opcionesMenu.add_command(label="Tipo de Calculadora", command=Proximamente)
opcionesMenu.add_separator() #Agrega barritas separadoras
opcionesMenu.add_command(label="Salir", command=salirAplicacion)


"""

edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")
edicionMenu.add_separator()
edicionMenu.add_command(label="Deshacer")
edicionMenu.add_command(label="Rehacer")

vistasMenu=Menu(barraMenu, tearoff=0)
vistasMenu.add_command(label="Acercar")
vistasMenu.add_command(label="Alejar")
vistasMenu.add_command(label="Pantalla Completa")
"""

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Sobre este programa", command=infoAdicional)
ayudaMenu.add_command(label="Ayuda", command=Ayuda)

 

barraMenu.add_cascade(label="Opciones", menu=opcionesMenu)

 
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


############  FUNCIONES DE LOS BOTONES  ###########

def codigoBoton(a):
	
	global resultadoPrevioNum
	global numeroOperadores

	if resultadoPrevioNum:

		if type(a)==int or  "√":
			
			valorNumerico.set("")

		resultadoPrevioNum=False


	if a in ("+", "-","X","/","%", "√"):

		numeroOperadores+=1

	if (a==0 and valorNumerico.get()=="0")  :

		valorNumerico.set(a)

	else:

		if (a=="." and "." in valorNumerico.get()):

			if "+" in valorNumerico.get() or "-" in valorNumerico.get() or "X" in valorNumerico.get() or "/" in valorNumerico.get() or "%" in valorNumerico.get() or "√" in valorNumerico.get() in valorNumerico.get():
				
				if (a=="." and  valorNumerico.get().count(".")==numeroOperadores):
				
					valorNumerico.set(valorNumerico.get()+str(a))	
				
				else:
				
					valorNumerico.set(valorNumerico.get())
			
			else :
				
				valorNumerico.set(valorNumerico.get())

		else:		
		
			valorNumerico.set(valorNumerico.get() + str(a))

	

def borrarTotal():

	valorNumerico.set("")

def borrarNumero():

	valorNumerico.set(valorNumerico.get()[:-1])

def ANS():

	valorNumerico.set(valorNumerico + valorNumerico.get())

def calculaResultado():

	global resultadoPrevioNum
	global numeroOperadores

	valorNumerico.get() 
	operacion=str(valorNumerico.get() )

 
	try:

		if valorNumerico.get() == "27":

			messagebox.showinfo("Patata", "I see you are a men of culture as well")

		if valorNumerico.get() == "7":

			messagebox.showinfo("Patata 2: El regreso", "SIETEEEEEEEEEEEEE")


		if "+" in valorNumerico.get():

			suma=0

			for i in range (len(operacion.split("+"))):

				suma+= int(operacion.split("+")[i])

			valorNumerico.set(suma)
		
		elif "/" in valorNumerico.get():

			valorNumerico.set(int(operacion.split("/")[0]) / int(operacion.split("/")[1]))
		
		elif "%" in valorNumerico.get():

			valorNumerico.set(int(operacion.split("%")[0]) % int(operacion.split("%")[1]))

		elif "√" in valorNumerico.get():

			valorNumerico.set(math.sqrt(int(operacion.split("√")[1])))

		elif "x" in valorNumerico.get():

			multiplicacion=1

			for i in range (len(operacion.split("x"))):

				multiplicacion *= int(operacion.split("x")[i])

			valorNumerico.set(multiplicacion)

		elif "-" in valorNumerico.get():

			if operacion.split("-")[0]=="":

				resta=(-1)*int(operacion.split("-")[1])
				a=2

			else:
				resta=int(operacion.split("-")[0])

				a=1

			for i in range (a,len(operacion.split("-"))):

				resta-= int(operacion.split("-")[i])

			valorNumerico.set(resta)


		numeroOperadores+=1

	except IndexError:
		
		operacionErronea()

	except ValueError:
		
		operacionErronea()

	except ZeroDivisionError:
		
		divisionCero()

	resultadoPrevioNum=True
 
 
#################### NUMEROS ####################

botonNumero = Button(raiz, text = str(7), command = lambda: codigoBoton(7))
botonNumero.grid(row=1, column=0, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(8), command = lambda: codigoBoton(8))
botonNumero.grid(row=1, column=1, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(9), command = lambda: codigoBoton(9))
botonNumero.grid(row=1, column=2, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(4), command = lambda: codigoBoton(4))
botonNumero.grid(row=2, column=0, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(5), command = lambda: codigoBoton(5))
botonNumero.grid(row=2, column=1, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(6), command = lambda: codigoBoton(6))
botonNumero.grid(row=2, column=2, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(1), command = lambda: codigoBoton(1))
botonNumero.grid(row=3, column=0, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(2), command = lambda: codigoBoton(2))
botonNumero.grid(row=3, column=1, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(3), command = lambda: codigoBoton(3))
botonNumero.grid(row=3, column=2, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonNumero = Button(raiz, text = str(0), command = lambda: codigoBoton(0))
botonNumero.grid(row=4, column=0, padx=2, pady=5,sticky='EWNS')
botonNumero.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))


####################### OPERADORES ########################

botonOperacion = Button(raiz, text = "+", command = lambda: codigoBoton("+"))
botonOperacion.grid(row=1, column=3, padx=2, pady=5,sticky='EWNS')
botonOperacion.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonOperacion = Button(raiz, text = "/", command = lambda: codigoBoton("/"))
botonOperacion.grid(row=1, column=4, padx=2, pady=5,sticky='EWNS')
botonOperacion.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonOperacion = Button(raiz, text = "x", command = lambda: codigoBoton("x"))
botonOperacion.grid(row=2, column=4, padx=2, pady=5,sticky='EWNS')
botonOperacion.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonOperacion = Button(raiz, text = "-", command = lambda: codigoBoton("-"))
botonOperacion.grid(row=2, column=3, padx=2, pady=5,sticky='EWNS')
botonOperacion.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonResto = Button(raiz, text = "%", command = lambda: codigoBoton("%"))
botonResto.grid(row=3, column=3, padx=2, pady=5,sticky='EWNS')
botonResto.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonOperacion = Button(raiz, text = "√", command = lambda: codigoBoton("√"))
botonOperacion.grid(row=3, column=4, padx=2, pady=5,sticky='EWNS')
botonOperacion.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonPotencia = Button(raiz, text = ".", command = lambda: codigoBoton("."))
botonPotencia.grid(row=4, column=1, padx=2, pady=5,sticky='EWNS')
botonPotencia.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonBorrar = Button(raiz, text = "Borrar", command = borrarTotal)
botonBorrar.grid(row=4, column=2, padx=2, pady=5,sticky='EWNS')
botonBorrar.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 23))

botonBorrar = Button(raiz, text = "🡐", command = borrarNumero)
botonBorrar.grid(row=4, column=3, padx=2, pady=5,sticky='EWNS')
botonBorrar.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))

botonOperacion = Button(raiz, text = "=", command = calculaResultado)
botonOperacion.grid(row=4, column=4, padx=2, pady=5,sticky='EWNS')
botonOperacion.config(width=4, height=2, bg="#84ff00", font=("Arial Black", 30))



 

raiz.mainloop()