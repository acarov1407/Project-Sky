from tkinter import filedialog
from tkinter import Tk 
import json
from os import remove

class MyFile:
    
    '''Controla todas las operaciones
    relacionadas con archivos'''

    TITLE_PROGRAMPATH_PATH = "src/FileData/PROGRAMS_PATHS.json"

    def get_folder_path_interface(self):

        '''Esta función abre un explorador de 
        archivos y guarda la ruta seleccionada
        por el usuario(carpetas)'''

        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askopenfilename()
        return folder_selected

    def get_file_path_interfaz(self):

        '''Esta funcion abre un explorador de archivos y guarda la ruta
        seleccionada por el usuario (archivos)'''

        root = Tk()
        root.withdraw()
        file_selected = filedialog.askopenfilename()
        return file_selected

    def save_location_to_file(self,file_header,file_path,save_in):

        '''Esta función toma una pareja (header,path) y la 
        guarda en el archivo especificado'''

        data_dict = self.read_file(save_in)
        data_dict[file_header.upper()] = file_path
        self.write_file(data_dict,save_in)

    def write_file(self,dictionary,file_name):

        '''Esta función guarda un diccionario dentro
        de un archivo .json'''

        try:
            with open(file_name,"w") as outfile:
                outfile.write(json.dumps(dictionary,indent=2))
        
        except Exception as e:
            print(e)
            return False
    
    def read_file(self,file_name):

        '''Esta funcion lee un archivo .json y 
        guarda el contenido en un diccionario'''

        try:
            with open(file_name,"r") as infile:
                res = infile.read()
                return json.loads(res)
        
        except Exception as e:
            print(e)
            return {0:0}

    def search_file_path(self,search_title,file_name):

        '''Esta función toma un titulo o key y 
        regresa la ruta/path'''

        title_in_file = search_title.upper()
        data = self.read_file(file_name)

        if title_in_file in data:
            return data[title_in_file]
        else:
            return False

    def delete_file(self,file_name):

        '''Esta función elimina todo el contenido
        de un archivo .json pero sin eliminar
        el archivo'''

        try:
            remove(file_name)
            with open(file_name,"w") as outfile:
                d = {}
                outfile.write(json.dumps(d,indent=2))
        
        except Exception as e:
            print(e)




    
                
