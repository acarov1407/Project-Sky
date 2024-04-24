from pynput import keyboard
from Command import Command
from gui.gui_main import MainGUI
from threading import Thread
from time import sleep
from MyReminder import ReminderRetrieve
from MP3Player import MP3Player


def wait_for_key():
    with keyboard.Listener(on_press= on_press) as listener:
        listener.join()

def on_press(key):
    if key == keyboard.Key.alt_l:
        com = Command('¿Que deseas?')

        #Update label main GUI Thread
        t_update = Thread(target=Mgui.update_label, args=(com.command_text, ))
        t_update.start()
        com.command_selection()
        sleep(2)
        Mgui.root.withdraw()






Mgui = MainGUI()

#Reminders
reminders = ReminderRetrieve()

#Main Thread
t_main = Thread(target=wait_for_key)
t_main.start()

#Main GUI Thread
t_gui = Thread(target= Mgui.run, args=('Presiona "ALT" para decir un comando', ))
t_gui.start()

#Records Thread
t_records = Thread(target=reminders.run)
t_records.start()


