from MyFile import MyFile
import os
from VoiceRecord import Voice

class Program(MyFile):

    '''Clase encargada de manejar interacción del
    usuario con respecto a programas .exe'''

    def __init__(self, name, path= False):

        self.name = name
        self.path = path

    def open(self):

        '''Esta funcion intenta abrir un programa a partir de una 
        ruta/path. Si no logra abrirlo significa que no hay permisos
        o no ha sido previamente configurado el programa y la ruta'''

        try:
            os.startfile(self.path)
            voz = Voice()
            voz.answer_voice("Abriendo: " + self.name.lower(), voz.MP3_VOICE)
        
        except PermissionError:

            voz = Voice()
            voz.answer_voice("Acceso Denegado",voz.MP3_VOICE)

        except:
            return False

    def config_path(self):

        '''Esta funcion abre un explorador de archivos y guarda la ruta/path'''

        try:
            self.path = self.get_file_path_interfaz()
        
        except Exception as e:
            self.path = False
            print(e)
    
    def ask_if_save(self, bool_ask):

        '''Esta funcion pregunta al usuario si queire guardar la configuracion
        del programa.
        Si--> Guarda la ruta/path al archivo PROGRAMS_PATHS.json
        No--> Retorna falso y termina'''

        voz = Voice()

        if bool_ask:
            self.config_path()
            self.save_location_to_file(self.name,self.path,self.TITLE_PROGRAMPATH_PATH)
            voz.answer_voice("Configuracion guardada",voz.MP3_VOICE)

        else:
            voz.answer_voice("Ha decidido no guardar la configuracion",voz.MP3_VOICE)
            return False