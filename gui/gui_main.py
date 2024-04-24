from tkinter import Tk, StringVar, Label, CENTER, Button
import sys

class MainGUI:


    def run(self, msg):
        
        self.root = Tk()
        self.initial_message = msg
        
        #Atributtes
        self.root.attributes("-topmost", True)
        #self.root.resizable(False, False)
        self.root.configure(bg="#424949")
        self.root.iconbitmap('src/icons/iron_man.ico')
        self.root.title('Sky')

        #Size of Main Frame
        width = 300
        height = 70

        #Position
        window_width = self.root.winfo_reqwidth()
        pos_horizontal = int(self.root.winfo_screenwidth()/2 - window_width/2)
        pos_vertical = 0
        self.root.geometry("{}x{}+{}+{}".format(width, height, pos_horizontal, pos_vertical))

        self.set_labels()
        self.root.withdraw()
        self.root.mainloop()

    def set_labels(self):

        self.label_command = Label(self.root, text=self.initial_message, font=("Bahnschrift Condesed", "9", "bold"), bg="#424949", fg="#F4F6F7")
        self.label_command.place(relx=0.5, rely=0.5, anchor=CENTER)


    
    #------------------------------------ENGINE FUNCTIONS-----------------------------------
    def update_label(self, msg):

        self.label_command['text'] = msg
        self.root.deiconify()







