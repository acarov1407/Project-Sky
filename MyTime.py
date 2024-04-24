import time
from MyFile import MyFile

class MyTime:

    '''Clase encargada de manejar hora y fecha'''

    TIME_PATH = "src/FileData/TIME_DATA.json"

    Mfile = MyFile()

    #Diccionario que contiene elementos necesarios para procesar la
    #hora y fecha de máquina a un entendimiento amigable con el usuario
    data_time = Mfile.read_file(TIME_PATH) 

    def __init__(self):

        '''Constructor de la clase. Toma la hora y fecha
        en formato extenso/máquina y la convierte en formato
        estandar'''

        LFT = time.localtime() #LFT --> Local Full Time

        time_hour = time.strftime("%I:%M %p", LFT)

        date = LFT[6],LFT[2],LFT[1],LFT[0]

        self.full_time = LFT
        self.hour = time_hour
        self.date = date
    
    def get_hour(self):

        return "Son las {} {} {}".format(self.hour[:2],self.hour[3:5],self.hour[6:])

    def get_date(self):

        return "Hoy es {}, {} de {} de {}".format(self.data_time["DayText"][str(self.date[0])],self.date[1],
        self.data_time["MonthText"][str(self.date[2])],self.date[3])

    def get_format_date(self, strdate):
        
        #Funcion que toma cadena de texto en formato humano con la informacion
        #de una fecha especifica y la transforma en formato maquina
        
        strdate = strdate.split()
        for item in strdate:
            try:
                day = int(item)
            except:
                pass
            
            if len(item) > 3:
                month = item
        
        month = self.month_to_number(month)
        date_formated = str(self.date[3]) + '-' + str(month) + '-' + str(day)
        return date_formated

    def get_format_hour(self,strhour):
        
        #Funcion que toma cadena de texto en formato humano con la informacion
        #de una hora especifica y la transforma en formato maquina
        
        try:
            strhour = strhour.split()
            c = ''
            for item in strhour:
                if len(item) <= 3 and 'p.m.' not in item and 'a.m.' not in item:
                    pass
                else:
                    c = c + item
            c = c.upper()
            c = c.replace('.','')
            return c
        
        except:
            return False
        

    def month_to_number(self,strmonth):

        #Funcion que toma una cadena de texto con el nombre de un mes y devuelve 
        #el numero de mes. Ej input(octubre) output(10)
        try:
            strmonth = strmonth.upper()
            for m in self.data_time["MonthToNumber"]:
                if m in strmonth:
                    return self.data_time["MonthToNumber"][m]
            return False
        
        except:
            return False
        





