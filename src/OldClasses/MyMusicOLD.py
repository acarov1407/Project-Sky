import os
import urllib.parse
import youtube_dl
from VoiceRecord import Voice
from unidecode import unidecode
from MyFile import MyFile
import pywhatkit

#++++
#++++ CLASE FUERA DE SERVICIO A LA FECHA 05/07/2022
#++++
class MyMusic:

    '''Clase encargada de manejar la descarga de canciones desde 
    youtube y ubicarlas en la carpeta correspondiente'''

    SAVED_MUSIC_PATH = "Music"
    AVAILABLE_SONGS_PATH = "FileData/MUSIC_DATA.json"

    def __init__(self,title,author=""):
        self.title = title
        self.author = author
        self.url = self.get_url()

    def get_url(self):

        #Funcion encargada de buscar el titulo de la cancion en youtube
        #para luego retornar su url correspondiente

        songname = self.title + self.author
        query_string = urllib.parse.urlencode({'search_query':songname})
        html_response = urllib.request.urlopen("https://www.youtube.com/results?" + 
        query_string)
        decoded_response_str = str(html_response.read().decode())
        html_response.close()
        splited_response_str = decoded_response_str.split('{"webCommandMetadata":{"url":"')

        for word in splited_response_str:
            if word[0:9] == "/watch?v=":
                return "https://www.youtube.com/watch?v=" + word[9:20]
        return False

    def download(self,downloadcheck=True):

        #Funcion encargada de descargar cualquier video de youtube
        #a partir de su url
        
        url_song = self.url
        video_info = youtube_dl.YoutubeDL().extract_info(url = url_song, download=False)
        temp_name = f"{video_info['title']}.mp3"
        self.filename = unidecode(temp_name)

        if downloadcheck:
            voz = Voice()
            voz.answer_voice("Descargando...",voz.MP3_VOICE)

            options = {
                'format' : 'bestaudio/best',
                'keepvideo' : False,
                'outtmpl' : self.filename,
                'postprocessors' : [{
                    'key' : 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
    
            try:
                with youtube_dl.YoutubeDL(options) as ydl:
                    try:
                        ydl.download([video_info['webpage_url']])
                    except:
                        print("Error en formato")
                    move_command = "move " + '"' + self.filename + '"' + " " + self.SAVED_MUSIC_PATH
                    mfile = MyFile()
                    mfile.save_location_to_file(self.filename,self.filename,self.AVAILABLE_SONGS_PATH)
                    os.system(move_command)

            except Exception as e:
                print("Error en la descarga ",e)
    
        else:
            return self.filename

    def check_available_songs(self):

        #Funcion encargada de leer el archivo de registro de canciones
        #descargadas y guardar los titulos en un diccionario
        
        mfile = MyFile()
        songs_dict = mfile.read_file(self.AVAILABLE_SONGS_PATH)
        return songs_dict

    def play_music(self):

        #Funcion encargada de reproducir la cancion solicitada por el usuario
        #siempre y cuando haya sido descargada previamente

        dict_songs = self.check_available_songs()
        song_name = self.download(False)

        if song_name.upper() in dict_songs:

            value = dict_songs[song_name.upper()]
            open_command = '"' + self.SAVED_MUSIC_PATH + '/' + value + '"'
            os.system(open_command)
        
        else:
            voz = Voice()
            voz.answer_voice("La canción no esta en tu biblioteca, buscando en youtube",voz.MP3_VOICE)
            pywhatkit.playonyt(song_name)
            

