from VoiceRecord import Voice
from MyFile import MyFile
import datetime
from MyTime import MyTime
from time import sleep

RECPATH = 'src/FileData/REMINDERS.json'

class Reminder:
    
    '''Clase que maneja el procesamiento de los recordatorios y los guarda en el archivo correspondiente'''

    #------------------------------------------------------PROCESS AND SAVE REMINDER-----------------------------------------------------------
    def __init__(self, body, date_sf, hour_sf='12:00PM'):
        self.body = body
        self.date_sf = date_sf
        self.hour_sf = hour_sf

        self.process_record()

    def save_record(self,cuerpo,fecha,hora='12:00 PM'):

        #Guarda el recordatorio en el archivo de recordatorios

        headkey = fecha + '&' + hora
        f = MyFile()
        f.save_location_to_file(headkey,cuerpo, RECPATH)


    def body_filter(self):

        #Filtra palabras innecesarias para el cuerpo del recordatorio.

        self.body = self.body.lower()
        filter_words = ['que', 'tengo', 'debo']
        for w in filter_words:
            if w in self.body:
                self.body = self.body.replace(w, '')
        
    def process_record(self):
        
        #Funcion que toma el recordatorio en formato humano
        #y lo transforma en un formato apto para guardar en archivo

        #Procesar Cuerpo
        self.body_filter()

        #Procesar fecha y hora
        if 'manana' in self.date_sf.lower():
            tm = MyTime()
            date = str(datetime.date.today() + datetime.timedelta(days=1))
            hour = tm.get_format_hour(self.hour_sf)
        
        elif 'hoy' in self.date_sf.lower():
            tm = MyTime()
            date = str(datetime.date.today())
            hour = tm.get_format_hour(self.hour_sf)
        else:
            tm = MyTime()
            date = tm.get_format_date(self.date_sf)
            hour = tm.get_format_hour(self.hour_sf)
            
        self.save_record(self.body,date,hour)
        v = Voice()
        v.answer_voice('Recordatorio Guardado', v.MP3_VOICE)
    
    #--------------------------------------------------------------------------------------------------------------------------------



    #------------------------------------------------------RETRIEVE REMINDER-----------------------------------------------------------

class ReminderRetrieve:

    '''Clase encargada de la recuperacion de los recordatorios del archivo para
        notificar al usuario cuando sea necesario'''

    TIMES = 0

    def process_reminder(self, reminder):

        #Funcion que toma un solo recordatorio en formato archivo y lo
        #procesa para que quede de la forma (body, date, hour)

        date_hour = datetime.datetime.strptime(reminder, '%Y-%m-%d&%I:%M%p')
        return date_hour.strftime('%Y-%m-%d %I:%M%p')

    def check_reminders(self):

        #Funcion que se encarga de revisar si hay algun recordatorio listo para
        #ser notificado al usuario
        
        v = Voice()
        f = MyFile()
        
        reminders = f.read_file(RECPATH)
        for reminder in reminders:
            temp_reminder = self.process_reminder(reminder)
            if temp_reminder == datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p'):
                self.TIMES += 1
                if self.TIMES <=3:
                    v.answer_voice('Recordatorio: ' + reminders[reminder], 'reminder.mp3')
                else:
                    self.TIMES = 0
                    sleep(52)
                return reminders[reminder]

    def clean_reminders(self):

        #Funcion que elimina los recordatorios que ya pasaron
        pass

    def run(self):
        while True:
            try:
                self.check_reminders()
            except:
                print('Excepción al revisar los recordatorios')

            sleep(3)




        
            


    
