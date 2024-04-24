from MyFile import MyFile
from VoiceRecord import Voice
import os
class GoogleSearch:
    
    '''Clase encargada de las busquedas en Google'''
    
    INTERNET_SEARCH_PATH = 'src/FileData/INTERNET_SEARCHES.json'

    def go_search(self, search_title):
        
        '''Función que toma el titulo de una busqueda.
        1. Si encuentra el titulo en el archivo de busquedas, abre directamente el link configurado
        2. Si no lo encuentra hace la búsqueda directamente en el buscador de Google'''

        mfile = MyFile()
        v = Voice()

        configured_searches = mfile.read_file(self.INTERNET_SEARCH_PATH)

        if search_title in configured_searches:
            os.system("start " + configured_searches[search_title])
            v.answer_voice("Abriendo busqueda configurada: " + search_title, v.MP3_VOICE)
        else:
            v.answer_voice("Mostrando resultados en google",v.MP3_VOICE)
            search_title = search_title.lower()
            search_title = search_title.replace(" ","+")
            os.system("start https://www.google.com/search?q=" + search_title)