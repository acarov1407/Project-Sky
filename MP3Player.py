from tkinter import HORIZONTAL, RAISED, PhotoImage, Tk, Button, Frame, Label, Scale, GROOVE, RAISED, Toplevel
import pygame
import random
from MyFile import MyFile

class MP3Player:

    DEFAULT_VOLUME = 0.4
    DEFAULT_MUSIC_PATH = 'Music/'
    AVAILABLE_SONGS_PATH = "src/FileData/MUSIC_DATA.json"


    def __init__(self, minimized = False):
        
        pygame.init()
        pygame.mixer.init()
        self.first_time = True
        self.paused = True
        self.is_random = False
        self.stepper = 0
        self.songs = list(self.check_available_songs().values())
        self.minimized = minimized

    
        
   
    
    def run(self):

        #Attributes     
        self.root = Tk()
        self.root.configure(bg="#F4F6F7")
        self.root.iconbitmap('src/icons/music.ico')
        self.root.title('MP3 Player')
        
        #Size of Main Frame
        width = 300
        height = 95

        #Position
        self.root.geometry("{}x{}-0-32".format(width, height))

        #Load Widgets
        self.load_labels()
        self.load_buttons()
        self.load_scale()

 
        #Run GUI
        self.root.after(1000, self.check_if_finished)
        self.root.after(1, self.minimize)
        self.root.mainloop()

    def minimize(self):
        
        if self.minimized:
            self.root.iconify()

    def load_buttons(self):
        
        #Frame
        buttons_frame = Frame(self.root, bg='#F4F6F7')
        buttons_frame.pack()
        
        #Button Images
        self.random_btn_img = PhotoImage(file='src/images/random.png')
        self.back_btn_img = PhotoImage(file='src/images/back.png')
        self.play_btn_img = PhotoImage(file='src/images/play.png')
        self.pause_btn_img = PhotoImage(file='src/images/pause.png')
        self.next_btn_img = PhotoImage(file='src/images/next.png')

        #Buttons
        self.random_btn = Button(buttons_frame, image=self.random_btn_img, command=self.random_f, bg='#F0F3F4')
        self.back_btn = Button(buttons_frame, image=self.back_btn_img, command=self.previous, bg='#F0F3F4')
        self.play_btn = Button(buttons_frame, image=self.play_btn_img, command=self.play, bg='#F0F3F4')
        self.pause_btn = Button(buttons_frame, image=self.pause_btn_img, command=self.pause, bg='#F0F3F4')
        self.next_btn = Button(buttons_frame, image=self.next_btn_img, command=self.next, bg='#F0F3F4')

        self.random_btn.grid(row=0, column=0, padx=5, pady=5)
        self.back_btn.grid(row=0 , column= 1, padx=5, pady=5)
        self.play_btn.grid(row=0, column=2, padx=5, pady=5)
        self.pause_btn.grid(row=0, column=3, padx=5, pady=5)
        self.next_btn.grid(row=0, column=4, padx=5, pady=5)


    def load_labels(self):

        label_frame = Frame(self.root, bg='#F4F6F7', pady=5)
        label_frame.pack()

        self.song_lbl = Label(label_frame, text='Sin Canciones', font=("Bahnschrift Condesed", "9", "bold"), bg='#F4F6F7')
        self.song_lbl.pack()

        

    def load_scale(self):

        #Scale Frame
        scale_frame = Frame(self.root, bg='#F4F6F7')
        scale_frame.pack()

        #Volume Image Setting
        self.volume_lbl_img = PhotoImage(file='src/images/volume.png')
        self.volume_lbl = Label(scale_frame, image=self.volume_lbl_img)
        self.volume_lbl.grid(row=0, column= 0)

        #Scale Setting
        self.volume_scl = Scale(scale_frame, from_=0, to=100, orient=HORIZONTAL, width=10, bg='#F4F6F7', showvalue=False, command=self.set_volume)
        self.volume_scl.set(self.DEFAULT_VOLUME*100)
        self.volume_scl.grid(row=0, column=1)

    

    def random_f(self):
        
        if self.is_random:
            self.is_random = False
            self.random_btn.config(relief=RAISED, bg='#F0F3F4')
        else:
            self.is_random = True
            self.random_btn.config(relief=GROOVE, bg='#D0D3D4')

    def load_play(self, start_in_song = None):
        
        if start_in_song is None:
            try:
                pygame.mixer.music.load('Music/' + self.songs[self.stepper])
                pygame.mixer.music.play()
            except Exception as e:
                print('Excepcion el MP3Player - loadplay()' + e)
                self.stepper = 0
                pygame.mixer.music.load('Music/' + self.songs[self.stepper])
                pygame.mixer.music.play()
        
            self.song_lbl['text'] = self.songs[self.stepper].replace(".mp3", "")

        else:

            try:
                pygame.mixer.music.load('Music/' + start_in_song)
                pygame.mixer.music.play()
                #self.song_lbl['text'] = start_in_song.replace(".mp3", "")
            
            except Exception as e:
                print('Excepcion en MP3Player - loadplay() ' + e)

    def play(self, start_in_song = None):

        if self.is_random:
            self.stepper = random.randint(0, len(self.songs) - 1)

        try:
            self.paused = False

            if self.first_time:
            
                pygame.mixer.music.set_volume(self.DEFAULT_VOLUME)
                self.first_time = False

                if start_in_song is None:
                    self.load_play()
                else:
                    self.load_play(start_in_song)
            else:
                self.resume()
        except Exception as e:
            print('Excepcion en MP3Player - play() ' + e)
    

    def pause(self):

        try:
            pygame.mixer.music.pause()
            self.paused = True
        except Exception as e:
            print('Excepcion en MP3Player - pause() ' + e)
        
    
    def resume(self):
        
        try : pygame.mixer.music.unpause()
        except: pass

    def next(self):
        
        try:
            self.paused = False
            pygame.mixer.music.stop()

            if self.is_random:
                actual_stepper = self.stepper
                self.stepper = random.randint(0, len(self.songs) - 1)
                while actual_stepper == self.stepper:
                    self.stepper = random.randint(0, len(self.songs) - 1)
            else:
                self.stepper +=1
        except Exception as e:
            print('Excepcion en MP3Player - next() ' + e)

        self.load_play()

    def previous(self):
        
        self.paused = False
        self.stepper -=1

        try:
            pygame.mixer.music.stop()
        except Exception as e:
            print('Excepcion en MP3Player - previous() ' + e)
            self.stepper = 0

        self.load_play()

    def set_volume(self, event):

        try:
            vol = self.volume_scl.get() / 100
            pygame.mixer.music.set_volume(vol)
        except Exception as e:
            print("Error al modificar el volumen: " + e)
        
        



    def check_if_finished(self):
        if self.paused or pygame.mixer.music.get_busy():
            pass
        else:
            self.next()
        self.root.after(1000, self.check_if_finished)


    def check_available_songs(self):

        #Funcion encargada de leer el archivo de registro de canciones
        #descargadas y guardar los titulos en un diccionario
        
        mfile = MyFile()
        songs_dict = mfile.read_file(self.AVAILABLE_SONGS_PATH)
        return songs_dict

#MP3Player("Soda Stereo - Signos (Gira Me Veras Volver).mp3", "Signos").run()
#MP3Player().run()