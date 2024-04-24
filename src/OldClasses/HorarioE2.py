from __future__ import division, unicode_literals
from tkinter import *
from tkinter import messagebox
from MyFile import MyFile
import codecs
from bs4 import BeautifulSoup
import datetime
import calendar

class HorarioEngine:

    def save_subject(self, button_invoc, data, window=""):

        file = MyFile()
        file.save_location_to_file(
            button_invoc, data, "HorarioData/HORARIO.json")

        if window != "":
            messagebox.showinfo("Asignatura", "Datos Guardados!")

        self.load_subjects()

        try:
            window.destroy()
        except:
            pass

    def load_subjects(self):

        try:
            file = MyFile()
            data = file.read_file("HorarioData/HORARIO.json")

            for item in data:
                if item == "SM1":
                    self.sm1['text'] = data[item]["ASIGNATURA"]
                if item == "SM2":
                    self.sm2['text'] = data[item]["ASIGNATURA"]

                if item == "SM3":
                    self.sm3['text'] = data[item]["ASIGNATURA"]
                if item == "SM4":
                    self.sm4['text'] = data[item]["ASIGNATURA"]
                if item == "SM5":
                    self.sm5['text'] = data[item]["ASIGNATURA"]
                if item == "SM6":
                    self.sm6['text'] = data[item]["ASIGNATURA"]
                if item == "SM7":
                    self.sm7['text'] = data[item]["ASIGNATURA"]
                if item == "ST1":
                    self.st1['text'] = data[item]["ASIGNATURA"]
                if item == "ST2":
                    self.st2['text'] = data[item]["ASIGNATURA"]
                if item == "ST3":
                    self.st3['text'] = data[item]["ASIGNATURA"]
                if item == "ST4":
                    self.st4['text'] = data[item]["ASIGNATURA"]
                if item == "ST5":
                    self.st5['text'] = data[item]["ASIGNATURA"]
                if item == "ST6":
                    self.st6['text'] = data[item]["ASIGNATURA"]
                if item == "ST7":
                    self.st7['text'] = data[item]["ASIGNATURA"]
                if item == "SW1":
                    self.sw1['text'] = data[item]["ASIGNATURA"]
                if item == "SW2":
                    self.sw2['text'] = data[item]["ASIGNATURA"]
                if item == "SW3":
                    self.sw3['text'] = data[item]["ASIGNATURA"]
                if item == "SW4":
                    self.sw4['text'] = data[item]["ASIGNATURA"]
                if item == "SW5":
                    self.sw5['text'] = data[item]["ASIGNATURA"]
                if item == "SW6":
                    self.sw6['text'] = data[item]["ASIGNATURA"]
                if item == "SW7":
                    self.sw7['text'] = data[item]["ASIGNATURA"]
                if item == "STH1":
                    self.sth1['text'] = data[item]["ASIGNATURA"]
                if item == "STH2":
                    self.sth2['text'] = data[item]["ASIGNATURA"]
                if item == "STH3":
                    self.sth3['text'] = data[item]["ASIGNATURA"]
                if item == "STH4":
                    self.sth4['text'] = data[item]["ASIGNATURA"]
                if item == "STH5":
                    self.sth5['text'] = data[item]["ASIGNATURA"]
                if item == "STH6":
                    self.sth6['text'] = data[item]["ASIGNATURA"]
                if item == "STH7":
                    self.sth7['text'] = data[item]["ASIGNATURA"]
                if item == "SF1":
                    self.sf1['text'] = data[item]["ASIGNATURA"]
                if item == "SF2":
                    self.sf2['text'] = data[item]["ASIGNATURA"]
                if item == "SF3":
                    self.sf3['text'] = data[item]["ASIGNATURA"]
                if item == "SF4":
                    self.sf4['text'] = data[item]["ASIGNATURA"]
                if item == "SF5":
                    self.sf5['text'] = data[item]["ASIGNATURA"]
                if item == "SF6":
                    self.sf6['text'] = data[item]["ASIGNATURA"]
                if item == "SF7":
                    self.sf7['text'] = data[item]["ASIGNATURA"]

        except:
            pass

    def load_from_web(self):

        file = MyFile()

        
        path = file.get_file_path_interfaz()

        try:
        
            f = codecs.open(path, 'r', 'utf-8')
            read = f.read()

        except:

            read = ""
            
        document = BeautifulSoup(read, "html.parser")
        horario = []
        for item in document.find_all(class_="af_calendar_time-activities-cell"):
            fecha = str(item)[15:25]
            for item2 in item.find_all(class_="af_calendar_time-activity-outer-container"):
                for item3 in item2.find_all(class_="af_calendar_time-activity-container"):

                    materia = str(item3).split(">")[4].replace("</dd", "")
                    hora = str(item3).split(">")[2][0:5]
                    full = []
                    full.append(fecha)
                    full.append(materia)
                    full.append(hora)
                    horario.append(full)

        for ful in horario:
            date = ful[0].replace("/", " ")
            ful[0] = self.findDay(date)
        return horario

    def set_from_web(self):

        horario_list = self.load_from_web()

        for group in horario_list:
            query = group[0] + " " + group[2]
            button_invoc = self.get_button_invoc(query)
            if button_invoc == "SM1":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "", 
                                                 "DIA": "Monday", "HOUR": "07:00"})
            if button_invoc == "SM2":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Monday", "HOUR": "09:00"})
            if button_invoc == "SM3":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Monday", "HOUR": "11:00"})
            if button_invoc == "SM4":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Monday", "HOUR": "14:00"})
            if button_invoc == "SM5":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Monday", "HOUR": "16:00"})
            if button_invoc == "SM6":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Monday", "HOUR": "18:00"})
            if button_invoc == "SM7":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Monday", "HOUR": "20:00"})
            if button_invoc == "ST1":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Tuesday", "HOUR": "07:00"})
            if button_invoc == "ST2":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Tuesday", "HOUR": "09:00"})
            if button_invoc == "ST3":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Tuesday", "HOUR": "11:00"})
            if button_invoc == "ST4":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Tuesday", "HOUR": "14:00"})
            if button_invoc == "ST5":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Tuesday", "HOUR": "16:00"})
            if button_invoc == "ST6":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Tuesday", "HOUR": "18:00"})
            if button_invoc == "ST7":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Tuesday", "HOUR": "20:00"})
            if button_invoc == "SW1":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Wednesday", "HOUR": "07:00"})
            if button_invoc == "SW2":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Wednesday", "HOUR": "09:00"})
            if button_invoc == "SW3":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Wednesday", "HOUR": "11:00"})
            if button_invoc == "SW4":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Wednesday", "HOUR": "14:00"})
            if button_invoc == "SW5":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Wednesday", "HOUR": "16:00"})
            if button_invoc == "SW6":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Wednesday", "HOUR": "18:00"})
            if button_invoc == "SW7":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Wednesday", "HOUR": "20:00"})
            if button_invoc == "STH1":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Thursday", "HOUR": "07:00"})
            if button_invoc == "STH2":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Thursday", "HOUR": "09:00"})
            if button_invoc == "STH3":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Thursday", "HOUR": "11:00"})
            if button_invoc == "STH4":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Thursday", "HOUR": "14:00"})
            if button_invoc == "STH5":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Thursday", "HOUR": "16:00"})
            if button_invoc == "STH6":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Thursday", "HOUR": "18:00"})
            if button_invoc == "STH7":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Thursday", "HOUR": "20:00"})
            if button_invoc == "SF1":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Friday", "HOUR": "07:00"})
            if button_invoc == "SF2":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Friday", "HOUR": "09:00"})
            if button_invoc == "SF3":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Friday", "HOUR": "11:00"})
            if button_invoc == "SF4":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Friday", "HOUR": "14:00"})
            if button_invoc == "SF5":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Friday", "HOUR": "16:00"})
            if button_invoc == "SF6":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Friday", "HOUR": "18:00"})
            if button_invoc == "SF7":
                self.save_subject(button_invoc, {"ASIGNATURA": group[1], "CODIGO": "",
                                                 "EDIFICIO": "", "SALON": "", "PROFESOR": "",
                                                 "DIA": "Friday", "HOUR": "20:00"})
        self.load_subjects()

    def get_button_invoc(self, day_hour_str):

        file = MyFile()
        button_invoc_dict = file.read_file("HorarioData/BUTTON_INVOC.json")
        if day_hour_str in button_invoc_dict:
            return button_invoc_dict[day_hour_str]
        else:
            return False

    def findDay(self, date):

        born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
        return (calendar.day_name[born])

class HorarioInterface(HorarioEngine):

    def load_init(self):

        self.root = Tk()
        self.root.configure(bg="#eceff1")
        self.set_labels()
        self.set_time_buttons()
        self.set_subject_buttons()
        self.load_subjects()
        self.set_activity_buttons()

        self.root.mainloop()

    def set_labels(self):

        self.label_time = Label(self.root, text="HORA", width=15, bg = "#cfd8dc",
                                fg = "#455a64", font=("Times New Roman", 14, "bold"))
        self.label_monday = Label(self.root, text="LUN", width=15,
                                  bg = "#cfd8dc", fg = "#455a64", font=("Times New Roman", 14, "bold"))
        self.label_tuesday = Label(self.root, text="MAR", width=15,
                                   bg = "#cfd8dc", fg = "#455a64", font=("Times New Roman", 14, "bold"))
        self.label_wednesday = Label(self.root, text="MIER", width=15,
                                     bg = "#cfd8dc", fg = "#455a64", font=("Times New Roman", 14, "bold"))
        self.label_thursday = Label(self.root, text="JUE", width=15,
                                    bg = "#cfd8dc", fg = "#455a64", font=("Times New Roman", 14, "bold"))
        self.label_friday = Label(self.root, text="VIE", width=15,
                                  bg="#cfd8dc", fg = "#455a64", font=("Times New Roman", 14, "bold"))

   
        self.label_time.grid(row=0, column=0, padx=15, pady=20)
        self.label_monday.grid(row=0, column=1, padx=15, pady=20)
        self.label_tuesday.grid(row=0, column=2, padx=15, pady=20)
        self.label_wednesday.grid(row=0, column=3, padx=15, pady=20)
        self.label_thursday.grid(row=0, column=4, padx=15, pady=20)
        self.label_friday.grid(row=0, column=5, padx=15, pady=20)


    def set_time_buttons(self):

        self.h1 = Button(self.root, text="7:00 - 9:00", width=15,
                         bg="#cfd8dc", fg="#37474f", font=("Times New Roman", 10, "bold"))
        self.h2 = Button(self.root, text="9:00 - 11:00", width=15,
                         bg="#cfd8dc", fg="#37474f", font=("Times New Roman", 10, "bold"))
        self.h3 = Button(self.root, text="11:00 - 13:00", width=15,
                         bg="#cfd8dc", fg="#37474f", font=("Times New Roman", 10, "bold"))
        self.h4 = Button(self.root, text="14:00 - 16:00", width=15,
                         bg="#cfd8dc", fg="#37474f", font=("Times New Roman", 10, "bold"))
        self.h5 = Button(self.root, text="16:00 - 18:00", width=15,
                         bg="#cfd8dc", fg="#37474f", font=("Times New Roman", 10, "bold"))
        self.h6 = Button(self.root, text="18:00 - 20:00", width=15,
                         bg="#cfd8dc", fg="#37474f", font=("Times New Roman", 10, "bold"))
        self.h7 = Button(self.root, text="20:00 - 22:00", width=15,
                         bg="#cfd8dc", fg="#37474f", font=("Times New Roman", 10, "bold"))

        self.h1.grid(row=1, column=0, pady=15)
        self.h2.grid(row=2, column=0, pady=15)
        self.h3.grid(row=3, column=0, pady=15)
        self.h4.grid(row=4, column=0, pady=15)
        self.h5.grid(row=5, column=0, pady=15)
        self.h6.grid(row=6, column=0, pady=15)
        self.h7.grid(row=7, column=0, pady=15)

    def set_subject_buttons(self):

        # MONDAY
        self.sm1 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sm1"))
        self.sm2 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sm2"))
        self.sm3 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sm3"))
        self.sm4 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sm4"))
        self.sm5 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sm5"))
        self.sm6 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sm6"))
        self.sm7 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sm7"))

        self.sm1.grid(row=1, column=1, pady=15)
        self.sm2.grid(row=2, column=1, pady=15)
        self.sm3.grid(row=3, column=1, pady=15)
        self.sm4.grid(row=4, column=1, pady=15)
        self.sm5.grid(row=5, column=1, pady=15)
        self.sm6.grid(row=6, column=1, pady=15)
        self.sm7.grid(row=7, column=1, pady=15)

        # TUESDAY

        self.st1 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("st1"))
        self.st2 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("st2"))
        self.st3 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("st3"))
        self.st4 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("st4"))
        self.st5 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("st5"))
        self.st6 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("st6"))
        self.st7 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("st7"))

        self.st1.grid(row=1, column=2, pady=15)
        self.st2.grid(row=2, column=2, pady=15)
        self.st3.grid(row=3, column=2, pady=15)
        self.st4.grid(row=4, column=2, pady=15)
        self.st5.grid(row=5, column=2, pady=15)
        self.st6.grid(row=6, column=2, pady=15)
        self.st7.grid(row=7, column=2, pady=15)

        # WEDNESDAY

        self.sw1 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sw1"))
        self.sw2 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sw2"))
        self.sw3 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sw3"))
        self.sw4 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sw4"))
        self.sw5 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sw5"))
        self.sw6 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sw6"))
        self.sw7 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sw7"))

        self.sw1.grid(row=1, column=3, pady=15)
        self.sw2.grid(row=2, column=3, pady=15)
        self.sw3.grid(row=3, column=3, pady=15)
        self.sw4.grid(row=4, column=3, pady=15)
        self.sw5.grid(row=5, column=3, pady=15)
        self.sw6.grid(row=6, column=3, pady=15)
        self.sw7.grid(row=7, column=3, pady=15)

        # THURSDAY

        self.sth1 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                           font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sth1"))
        self.sth2 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                           font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sth2"))
        self.sth3 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                           font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sth3"))
        self.sth4 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                           font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sth4"))
        self.sth5 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                           font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sth5"))
        self.sth6 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                           font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sth6"))
        self.sth7 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                           font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sth7"))

        self.sth1.grid(row=1, column=4, pady=15)
        self.sth2.grid(row=2, column=4, pady=15)
        self.sth3.grid(row=3, column=4, pady=15)
        self.sth4.grid(row=4, column=4, pady=15)
        self.sth5.grid(row=5, column=4, pady=15)
        self.sth6.grid(row=6, column=4, pady=15)
        self.sth7.grid(row=7, column=4, pady=15)

        # FRIDAY

        self.sf1 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sf1"))
        self.sf2 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sf2"))
        self.sf3 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sf3"))
        self.sf4 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sf4"))
        self.sf5 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sf5"))
        self.sf6 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sf6"))
        self.sf7 = Button(self.root, text="-----------", width=20, bg="#eceff1", fg="#263238",
                          font=("Georgia", 10,"bold"), command=lambda: self.config_subject("sf7"))

        self.sf1.grid(row=1, column=5, pady=15)
        self.sf2.grid(row=2, column=5, pady=15)
        self.sf3.grid(row=3, column=5, pady=15)
        self.sf4.grid(row=4, column=5, pady=15)
        self.sf5.grid(row=5, column=5, pady=15)
        self.sf6.grid(row=6, column=5, pady=15)
        self.sf7.grid(row=7, column=5, pady=15)

    def set_activity_buttons(self):

        self.lfw = Button(self.root, text="Cargar Horario desde HTML", bg="#263238", fg="#eceff1", font=(
            "Arial", 11, "bold"), command=self.set_from_web)
        self.lfw.grid(row=8, column=1, pady=15)

    def config_subject(self, button_invoc):

        subject_window = Toplevel(self.root)
        subject_window.configure(bg="#696969")

        Lsubject_code = Label(subject_window, text="Codigo Asignatura:",
                              bg="#455a64", fg="#eceff1", font=("Georgia", 10))
        Esubject_code = Entry(subject_window)

        Lsubject_name = Label(subject_window, text="Nombre Asignatura:*",
                              bg="#455a64", fg="#eceff1", font=("Georgia", 10))
        Esubject_name = Entry(subject_window)

        Ledifice_number = Label(subject_window, text="Edificio:",
                                bg="#455a64", fg="#eceff1", font=("Georgia", 10))
        Eedifice_number = Entry(subject_window)

        Lclassroom_number = Label(
            subject_window, text="Salón:", bg="#455a64", fg="#eceff1", font=("Georgia", 10))
        Eclassroom_number = Entry(subject_window)

        Lteacher = Label(subject_window, text="Profesor:",
                         bg="#455a64", fg="#eceff1", font=("Georgia", 10))
        Eteacher = Entry(subject_window)

        Bsave_subject = Button(subject_window, text="Guardar", bg="#eceff1", fg="#455a64", font=("Times New Roman", 10, "bold"), command=lambda: self.save_subject(
            button_invoc, {"ASIGNATURA": Esubject_name.get(), "CODIGO": Esubject_code.get(), "EDIFICIO": Eedifice_number.get(), "SALON": Eclassroom_number.get(), "PROFESOR": Eteacher.get()}, subject_window))

        Lsubject_name.grid(row=0, column=0, padx=10, pady=10)
        Esubject_name.grid(row=0, column=1, padx=10, pady=10)

        Lsubject_code.grid(row=1, column=0, padx=10, pady=10)
        Esubject_code.grid(row=1, column=1, padx=10, pady=10)

        Ledifice_number.grid(row=2, column=0, padx=10, pady=10)
        Eedifice_number.grid(row=2, column=1, padx=10, pady=10)

        Lclassroom_number.grid(row=3, column=0, padx=10, pady=10)
        Eclassroom_number.grid(row=3, column=1, padx=10, pady=10)

        Lteacher.grid(row=4, column=0, padx=10, pady=10)
        Eteacher.grid(row=4, column=1, padx=10, pady=10)

        Bsave_subject.grid(row=5, column=1, padx=10, pady=10)

