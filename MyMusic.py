from importlib.abc import MetaPathFinder
import os
import urllib.parse
from pytube import YouTube
from VoiceRecord import Voice
from unidecode import unidecode
from MyFile import MyFile
import pywhatkit
from helpers.Conversions import mp4_to_mp3
from threading import Thread
from MP3Player import MP3Player

class Song:

    '''Clase encargada de manejar la descarga de canciones desde 
    youtube y ubicarlas en la carpeta correspondiente'''

    SAVED_MUSIC_PATH = "Music"
    AVAILABLE_SONGS_PATH = "src/FileData/MUSIC_DATA.json"

    def __init__(self,title,author=""):

        if title != None:
            self.title = title
            self.author = author
            self.url = self.get_url()
        else:
            self.title = None
            self.author = None
            self.url = None

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

    def download(self):

        #Funcion encargada de descargar una cancion y guardarla
        #en la carpeta predefinida como mp3
        
        print('Descargando: ' + self.title)
        voz = Voice()
        voz.answer_voice('Descargando ' + self.title,voz.MP3_VOICE)
        
        #Create song
        yt = YouTube(self.get_url())

        #Get first song 
        video = yt.streams.filter(only_audio=True).first()

        try:
            #Save song to folder
            out_file = video.download(output_path=self.SAVED_MUSIC_PATH)
            
            #Convert to mp3 (Option 1)
            processed_filename = unidecode(out_file)
            os.rename(out_file, processed_filename)
            mp4_to_mp3(processed_filename)
            
            #Option 2 Convert to mp3
            #title,ext = os.path.splitext(out_file)
            #self.filename = title + '.mp3'
            #self.filename = unidecode(self.filename)
            #os.rename(out_file, self.filename)
            voz.answer_voice('Descarga exitosa' , voz.MP3_VOICE)

        except Exception as e:
            print(e)
            voz.answer_voice('Ha ocurrido un error al descargar la canción', voz.MP3_VOICE)
        
        
        save_name = os.path.basename(processed_filename).replace('.mp4', '.mp3')
        mfile = MyFile()
        mfile.save_location_to_file(unidecode(yt.title),save_name,self.AVAILABLE_SONGS_PATH)

    def check_available_songs(self):

        #Funcion encargada de leer el archivo de registro de canciones
        #descargadas y guardar los titulos en un diccionario
        
        mfile = MyFile()
        songs_dict = mfile.read_file(self.AVAILABLE_SONGS_PATH)
        return songs_dict

    def play_music(self, music_player : MP3Player = None):

        #Funcion encargada de reproducir la cancion solicitada por el usuario
        #siempre y cuando haya sido descargada previamente

        dict_songs = self.check_available_songs()

        #Create song
        yt = YouTube(self.get_url())

        #Get title 
        song_name = unidecode(yt.title)
      
 
        if song_name.upper() in dict_songs:
            
            value = dict_songs[song_name.upper()]
            
            if music_player is None:
                
                #Play in Windows player:
                open_command = '"' + self.SAVED_MUSIC_PATH + '/' + value + '"'
                os.system(open_command)
            else:

                #Play in OwnPlayer
                music_player.play(value)



            #Play in Windows player:
            #value = dict_songs[song_name.upper()]
            #open_command = '"' + self.SAVED_MUSIC_PATH + '/' + value + '"'
            #print(open_command)
            #os.system(open_command)
        
        else:
            voz = Voice()
            voz.answer_voice("La canción no esta en tu biblioteca, buscando en youtube",voz.MP3_VOICE)
            pywhatkit.playonyt(song_name)

