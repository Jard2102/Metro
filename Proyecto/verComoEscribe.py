import tkinter as tk

class AutocompleteEntry(tk.Entry):
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

def autocompletado(test_list):
    root = tk.Tk(className=' Así se escribe tu estación')
    root.geometry('+500+300')
    entry = AutocompleteEntry(
        root, 
        fg='white', bg='black',
        insertbackground='white', 
        font=('arial', 30))
    entry.set_completion_list(test_list)
    entry.grid()
    entry.focus_set()
    root.mainloop()

def main():
    Estaciones = [
    "Observatorio",
    "Tacubaya",
    "Juanacatlán",
    "Chapultepec",
    "Sevilla",
    "Insurgentes",
    "Cuauhtémoc",
    "Balderas",
    "Salto del Agua",
    "Isabel la Católica",
    "Pino Suárez",
    "Merced",
    "Candelaria",
    "San Lázaro",
    "Moctezuma",
    "Balbuena",
    "Boulevard Puerto Aéreo",
    "Gómez Farías",
    "Zaragoza",
    "Pantitlán",
    "Cuatro Caminos",
    "Panteones",
    "Tacuba",
    "Cuitláhuac",
    "Popotla",
    "Colegio Militar",
    "Normal",
    "San Cosme",
    "Revolución",
    "Hidalgo",
    "Bellas Artes",
    "Allende",
    "Zócalo",
    "Pino Suarez",
    "San Antonio Abad",
    "Chabacano",
    "Viaducto",
    "Xola",
    "Villa de Cortés",
    "Nativitas",
    "Portales",
    "Ermita",
    "General Anaya",
    "Tasqueña",
    "Indios Verdes",
    "Deportivo 18 de Marzo",
    "Potrero",
    "La Raza",
    "Tlatelolco",
    "Guerrero",
    "Hidalgo",
    "Juárez",
    "Balderas",
    "Niños Héroes",
    "Hospital General",
    "Centro Médico",
    "Etiopía/Plaza de la Transparencia",
    "Eugenia",
    "División del Norte",
    "Zapata",
    "Coyoacán",
    "Viveros/Derechos Humanos",
    "Miguel Ángel de Quevedo",
    "Copilco",
    "Universidad",
    "Martín Carrera",
    "Talismán",
    "Bondojito",
    "Consulado",
    "Canal del Norte",
    "Morelos",
    "Candelaria",
    "Fray Servando",
    "Jamaica",
    "Santa Anita",
    "Politécnico",
    "Instituto del Petróleo",
    "Autobuses del Norte",
    "La Raza",
    "Misterios",
    "Valle Gómez",
    "Consulado",
    "Eduardo Molina",
    "Aragón",
    "Oceanía",
    "Terminal Aérea",
    "Hangares",
    "Pantitlán",
    "El Rosario",
    "Tezozómoc",
    "Azcapotzalco",
    "Ferrería/Arena Ciudad de México",
    "Norte 45",
    "Vallejo",
    "Instituto del Petróleo",
    "Lindavista",
    "Deportivo 18 de Marzo",
    "La Villa-Basílica",
    "Martín Carrera",
    "El Rosario",
    "Aquiles Serdán",
    "Camarones",
    "Refinería",
    "Tacuba",
    "San Joaquín",
    "Polanco",
    "Auditorio",
    "Constituyentes",
    "Tacubaya",
    "San Pedro de los Pinos",
    "San Antonio",
    "Mixcoac",
    "Barranca del Muerto",
    "Garibaldi / Lagunilla",
    "Bellas Artes",
    "San Juan de Letrán",
    "Salto del Agua",
    "Doctores",
    "Obrera",
    "Chabacano",
    "La Viga",
    "Santa Anita",
    "Coyuya",
    "Iztacalco",
    "Apatlaco",
    "Aculco",
    "Escuadrón 201",
    "Atlalilco",
    "Iztapalapa",
    "Cerro de la Estrella",
    "UAM-I",
    "Constitución de 1917",
    "Tacubaya",
    "Patriotismo",
    "Chilpancingo",
    "Centro Médico",
    "Lázaro Cárdenas",
    "Chabacano",
    "Jamaica",
    "Mixiuhca",
    "Velodromo",
    "Ciudad Deportiva",
    "Puebla",
    "Pantitlán",
    "Pantitlán",
    "Agrícola Oriental",
    "Canal de San Juan",
    "Tepalcates",
    "Guelatao",
    "Peñón Viejo",
    "Acatitla",
    "Santa Marta",
    "Los Reyes",
    "La Paz",
    "Ciudad Azteca",
    "Plaza Aragón",
    "Olímpica",
    "Ecatepec",
    "Múzquiz",
    "Río de los Remedios",
    "Impulsora",
    "Nezahualcóyotl",
    "Villa de Aragón",
    "Bosque de Aragón",
    "Deportivo Oceanía",
    "Romero Rubio",
    "Ricardo Flores Magón",
    "San Lázaro",
    "Morelos",
    "Tepito",
    "Lagunilla",
    "Garibaldi",
    "Guerrero",
    "Buenavista",
    "Mixcoac",
    "Insurgentes Sur",
    "20 de Noviembre",
    "Zapata",
    "Parque de los Venados",
    "Eje Central",
    "Ermita",
    "Mexicaltzingo",
    "Atlalilco",
    "Culhuacán",
    "San Andrés Tomatlán",
    "Lomas Estrella",
    "Calle 11",
    "Periférico Oriente",
    "Tezonco",
    "Olivos",
    "Nopalera",
    "Zapotitlán",
    "Tlaltenco",
    "Tláhuac",
    ]

    Estaciones.sort(key = str)

    autocompletado(Estaciones)