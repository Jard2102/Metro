from tkinter import *
import os
import Metro
import verComoEscribe

class AutocompleteEntry(Entry):
    def set_completion_list(self, completion_list):
        self._completion_list = completion_list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def autocomplete(self):

        # set position to end so selection starts where textentry ended
        self.position = len(self.get())

        # collect hits
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()):
                _hits.append(element)

        # if we have a new hit list, keep this in mind 
        # if _hits != self._hits:
        self._hit_index = 0
        self._hits =_hits

        # # only allow cycling if we are in a known hit list
        # if _hits == self._hits and self._hits:
            # self._hit_index = (self._hit_index) % len(self._hits)

        # perform the auto completion
        if self._hits:
            self.delete(0,tk.END)
            self.insert(0,self._hits[self._hit_index])
            self.select_range(self.position,tk.END)

    def handle_keyrelease(self, event):
        if len(event.keysym) == 1:
            self.autocomplete()

def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

#VENTANA DE REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARACION "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARACION "sytring" COMO TIPO DE DATO PARA "clave"
 
    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()

    #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) 
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') 
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() #BOTÓN "Registrarse"

#VENTANA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.

    #VERIFICA QUE EL NOMBRE ESTE EN LA LISTA
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.

        if clave1 in verifica:
            exito_login() #EJECUTA FUNCIÓN "exito_login()"
        
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    menu_metro()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 
def menu_metro():
    global vent
    global estacion_inicial
    global estacion_destino
    global ordenamiento
    global entrada_inicio
    global entrada_destino
    global entrada_ordenamiento
    
    vent= Toplevel(ventana_login)
    vent.title("Bienvenido.")
    vent.geometry("300x250")

    Label(text = "Por favor, ingrese lo que se pide").pack()
    Label(text = "").pack()

    estacion_inicial = StringVar()
    estacion_destino = StringVar()

    Label(vent,text = "Estacion de salida").pack()
    entrada_inicio = Entry(vent, textvariable = estacion_inicial)
    entrada_inicio.pack()
    Label(vent, text = "").pack()

    Label(vent, text = "Estacion destino").pack()
    entrada_destino = Entry(vent, textvariable = estacion_destino)
    entrada_destino.pack()

    Label(vent, text = "").pack()
    Button(vent, text = "Registrar", width = 10, height = 1, command = registroEstaciones).pack()
    Label(vent, text = "").pack()
    Button(vent, text = "Acceder", width = 10, height = 1, command = llamarM).pack()
    Label(vent, text = "").pack()
    Button(vent, text = "Ver cómo se escribe tu estación", width = 28, height = 1, command = verEstacion).pack()

def registroEstaciones():
    inicio_info = estacion_inicial.get()
    destino_info = estacion_destino.get()
 
    file = open("estacion_inicial.txt", "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(inicio_info)

    file2 = open("estacion_destino.txt", "w")
    file2.write(destino_info)

    file.close()
    file2.close()

    Label(vent, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()

def verEstacion():
    verComoEscribe.main()

def llamarM():
    Metro.mainM()

ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.
 