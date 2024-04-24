from MyFile import MyFile
from VoiceRecord import Voice
from unidecode import unidecode
from MyTime import MyTime
from MyProgram import Program
from MyMusic import Song
from PCStatus import Usage, Monitor, Temperature
import sys 
import os
from MyReminder import Reminder
from MySearch import GoogleSearch
from MP3Player import MP3Player
from threading import Thread
#MP3Player Thread
ply = MP3Player(True)
t_mp3ply = Thread(target=ply.run)
t_mp3ply.start()

class Command(Voice):
    
    '''Hereda de Voice. Se encarga de controlar el 
    comando que recibe, y llama a la respectiva clase'''

    COMMAND_LIST_PATH = "src/FileData/COMMAND_LIST.json"

    def __init__(self,issue="No establecido"):
        
        self.commands_dict = self.get_command_list()
        self.answer_voice(issue,self.MP3_VOICE)
        self.command_text = self.voice_processing()


    def get_command_list(self):

        '''Lee el archivo que contiene todos los comandos validos
        y los guarda en un diccionario'''
        
        Mfile = MyFile()
        command_list = Mfile.read_file(self.COMMAND_LIST_PATH)
        return command_list

    def command_decode(self):

        '''Esta función toma el comando transformado en 
        texto, extrae el nombre del BOT dejando el
        comando en si'''

        split_command = self.command_text.split()
        just_command = " ".join(split_command[1:])

        #Importante devolver el comando en mayusculas
        return unidecode(just_command).upper() 

    def command_selection(self):

        '''FUNCIÓN MAS IMPORTANTE DE LA CLASE
            1. Busca el comando hecho texto en el diccionario
               de comandos válidos.
            2. Si encuentra el comando llama a la clase y función 
               correspondientes para ejecutar la tarea
            3. Si no encuentra el comando retorna un falso'''
        
        commandT1 = self.command_decode() #Comando literal
        commandT2 = commandT1.split() #Comando Dividido


        #-----------------------------------Cerrar Sky-----------------------------------
        if commandT1 in self.commands_dict["LITCOMMANDS"]["CERRAR"]:
            self.answer_voice("Adios señor",self.MP3_VOICE)
            sys.exit()
        
        #-----------------------------------Apagar Equipo-----------------------------------
        elif commandT1 in self.commands_dict["LITCOMMANDS"]["APAGAR"]:
            
            subcommand = SubCommand("¿Estas seguro?")
            
            if subcommand:
                self.answer_voice("Que descanse señor",self.MP3_VOICE)
                os.system("shutdown -s -t 5")
            else:
                pass

        #-----------------------------------Solicitar Hora-----------------------------------
        elif commandT1 in self.commands_dict["LITCOMMANDS"]["HORA"]:

            hour = MyTime()
            self.answer_voice(hour.get_hour(),self.MP3_VOICE)

        #-----------------------------------Solicitar Fecha-----------------------------------
        elif commandT1 in self.commands_dict["LITCOMMANDS"]["FECHA"]:

            date = MyTime()
            self.answer_voice(date.get_date(),self.MP3_VOICE)
        
        #-----------------------------------Ejecutar Aplicacion-----------------------------------
        elif commandT2[0] in self.commands_dict["KEYCOMMANDS"]["EJECUTAR"]:

            title = " ".join(commandT2[1:])

            if title == "":
                self.answer_voice("No me dijiste que abrir",self.MP3_VOICE)
            
            else:
                mfile = MyFile()
                path = mfile.search_file_path(title, mfile.TITLE_PROGRAMPATH_PATH)
                programa = Program(title,path)
                
                #Abre el archivo si el title esta en TITLE_PROGRAMPATH_PATH, si no lo hace, guarda en la
                #variable un valor de False
                success_open = programa.open() 

                if success_open == False:
                    command = SubCommand("Parece que lo que quieres abrir no ha sido configurado. ¿Deseas configurarlo ahora?")
                    result = command.command_selection()
                    programa.ask_if_save(result)
        
        #-----------------------------------Buscar en Internet-----------------------------------
        elif commandT2[0] in self.commands_dict["KEYCOMMANDS"]["BUSCARPAGINA"]:
            search_title = " ".join(commandT2[1:]).lower()
            GSearch = GoogleSearch()
            GSearch.go_search(search_title)

        #-----------------------------------Descargar Cancion-----------------------------------
        elif commandT2[0] in self.commands_dict["KEYCOMMANDS"]["DESCARGAR"]:

            song_name = " ".join(commandT2[1:])
            song = Song(song_name)
            song.download()

        #-----------------------------------Reproducir Cancion-----------------------------------
        elif commandT2[0] in self.commands_dict["KEYCOMMANDS"]["REPRODUCIR"]:

            song_name = " ".join(commandT2[1:])
            song = Song(song_name)
            song.play_music(ply)

        #-----------------------------------Controlar MP3Player-----------------------------------
        elif commandT1 in self.commands_dict["LITCOMMANDS"]["MP3PLAYER"]:
            action = commandT1
            if action == "SIGUIENTE":
                ply.next()
            elif action =="PAUSAR":
                ply.pause()
            elif action =="CONTINUAR":
                ply.resume()
            elif action =="ANTERIOR":
                ply.previous()
                
        elif commandT2[0] in self.commands_dict["KEYCOMMANDS"]["HARDWAREUSAGE"]:

            usg = Usage()
            print(commandT2)
            if "CPU" in commandT2: 
                self.answer_voice("Uso del cpu al " + str(usg.get_cpu_usage()) + "%",self.MP3_VOICE)
            elif "RAM" in commandT2:
                self.answer_voice("Uso de ram al " + str(usg.get_ram_usage()) + "%",self.MP3_VOICE)
            
        
        elif commandT2[0] in self.commands_dict["KEYCOMMANDS"]["HARDWARETEMP"]:
            temp = Temperature()
            print(commandT2)
            if "CPU" in commandT2 or "PROCESADOR" in commandT2:
                self.answer_voice("La temperatura del Cpu es de " + str(temp.get_cpu_temperature())+ "°C", self.MP3_VOICE)
            elif "GPU" in commandT2 or "TARJETA GRAFICA" in commandT2 or "GRAFICA" in commandT2:
                self.answer_voice("La temperatura de la Gpu es de " + str(temp.get_gpu_temperature())+ "°C", self.MP3_VOICE)
        elif commandT2[0] in self.commands_dict["KEYCOMMANDS"]["RECORDATORIO"]:
            cuerpo = " ".join(commandT2[1:])
            cuerpo = cuerpo.lower()
            respfecha = SubCommand('¿Cuando quieres que te lo recuerde?')
            fechastr = respfecha.command_selection()
            resphora = SubCommand('¿A que hora?')
            horastr = resphora.command_selection()
            Reminder(cuerpo, fechastr, horastr)
    


        else:
            print("Nada")
            self.answer_voice('No se ha entendido',self.MP3_VOICE)






class SubCommand(Command):

    '''Hereda de clase Command, encargada de recibir 
    una segunda respuesta por parte del usuario si
    es necesario'''

    def command_decode(self):

        '''Funcion overwrited, aca no es necesario eliminar
        la palabra clave del BOT puesto que no se dice'''

        return unidecode(self.command_text).upper()

    def command_selection(self):

        '''Funcion overwrited. Comandos especiales'''

        commandT1 = self.command_decode()

        if commandT1 in self.commands_dict["SUBCOMMANDS"]["AFIRMAR"]:
            return True
        
        elif commandT1 in self.commands_dict["SUBCOMMANDS"]["NEGAR"]:
            return False
        
        else:
            return commandT1
    

