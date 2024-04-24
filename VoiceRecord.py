import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from os import remove

class Voice:
    
    '''Clase encargada del reconocimiento y
    procesamiento de voz por parte del 
    usuario'''

    MP3_VOICE = "respuesta.mp3"
    
    def voice_record(self):

        '''Graba el microfono,recolecta
        el audio y devuelve un audio data'''

        r = sr.Recognizer()

        with sr.Microphone() as source:
            return r.listen(source,phrase_time_limit=4)
    
    def voice_to_text(self,voice_data):

        '''Toma un audio data y lo convierte
        en texto'''

        try:
            text_voice = sr.Recognizer().recognize_google(voice_data,language="es-Es")
            return text_voice
        
        except sr.UnknownValueError:
            text_voice = "No se ha entendido"
            return text_voice
        
        except sr.RequestError as e:
            return e

    def answer_voice(self,answer_text,file_name):

        '''Recibe una cadena de texto y la 
        reproduce como voz artificial'''
        tts = gTTS(answer_text,lang='es-us')
        tts.save(file_name)
        playsound(file_name)
        remove(file_name)

    def voice_processing(self):
        listener = sr.Recognizer()
        mic = sr.Microphone()

        try:
            with mic as source:
                voice = listener.listen(source,phrase_time_limit=4)
                text_voice = listener.recognize_google(voice,language="es-Es") 
                return text_voice

        except sr.UnknownValueError:
            text_voice = "No se ha entendido"
            return text_voice

        except sr.RequestError as e:
            return e


