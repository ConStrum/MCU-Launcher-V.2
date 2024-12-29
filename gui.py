import sys

import imp_functions

from PIL import Image
import customtkinter as ctk
from pywinstyles import set_opacity, apply_style
from pyglet import font

import config
from config import program_path

font.add_file(program_path + "\\font.ttf") # Titillium Web (Standard)



class FirstRunWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        font.add_file(program_path + "\\font.ttf")


        self.title(config.APP_TITLE)
        self.geometry(config.FIRST_WINDOW_SIZE)
        self.overrideredirect(True)
        self.configure(fg_color='black')
        self.resizable(False, False)
        self.attributes('-topmost', True)
        self.attributes('-topmost', False)
        self.attributes("-alpha", 0.0)



        self.custom_font = ctk.CTkFont("Titillium Web", size=15)


        self.background_image = Image.open(config.program_path + "\\images\\6.png")
        self.background_ctk = ctk.CTkImage(dark_image=self.background_image, size=(config.FIRST_WINDOW_SIZE_X, config.FIRST_WINDOW_SIZE_Y))
        self.background_label = ctk.CTkLabel(self, image=self.background_ctk, text="")


        self.logo_image = Image.open(config.program_path + "\\images\\logo.png")
        self.logo_ctk = ctk.CTkImage(dark_image=self.logo_image, size=(200, 200))
        self.logo_label = ctk.CTkLabel(self, image=self.logo_ctk, text="")
        set_opacity(self.logo_label, color="#000000")


        self.install_progressbar = ctk.CTkProgressBar(self, width=220, height=7, bg_color="#000001", progress_color="white", )
        self.install_progressbar.place(x=15, y=250)
        self.install_progressbar.set(0.0)
        set_opacity(self.install_progressbar, color="#000001")

        self.text_installing = ctk.CTkLabel(self, text="Vorbereitung...", width=220, height=9, bg_color="#000001", text_color="#6a7676")
        self.text_installing.place(x=15, y=260)
        set_opacity(self.text_installing, color="#000001")


        self.background_label.pack()
        self.logo_label.place(x=25, y=20)


        self.focus()


    def set_install_progressbar(self, progress_level: float):
        self.install_progressbar.set(progress_level)
        print("progressbar set to", progress_level)
    def StartFirstWindow(self):
        self.mainloop()
    def StopFirstWindow(self):
        self.destroy()
    def fade_in(self, current_alpha=0.0, step=0.005):
        if current_alpha < 1.0:
            current_alpha += step
            self.attributes("-alpha", current_alpha)
            self.after(4, self.fade_in, current_alpha)



class MainRunWindow(ctk.CTk):
    def __init__(self):

        super().__init__()

        font.add_file(program_path + "\\font.ttf")

        self.title(config.APP_TITLE)
        self.geometry(config.M_WINDOW_SIZE)
        self.resizable(False, False)
        self.iconbitmap(program_path + "\\icons\\icon256.ico")
        self.eval('tk::PlaceWindow . center')

        self.custom_font = ctk.CTkFont("Titillium Web")


        self.background_image = Image.open(config.program_path + "\\images\\4.png")
        self.background_ctk = ctk.CTkImage(dark_image=self.background_image, size=(config.M_WINDOW_SIZE_X, config.M_WINDOW_SIZE_Y))
        self.background_label = ctk.CTkLabel(self, image=self.background_ctk, text="")
        self.background_label.pack()



        self.pille_image = Image.open(config.program_path + "\\images\\pille.png")
        self.pille_ctk = ctk.CTkImage(dark_image=self.pille_image, size=(215, 65))
        self.pille_label = ctk.CTkLabel(self, image=self.pille_ctk, text="", bg_color="#000001")
        self.pille_label.place(x=50, y=605)

        set_opacity(self.pille_label,color="#000001")

        self.sound_button_image_unmute = Image.open(config.program_path + "\\icons\\unmute.png")
        self.sound_button_image_mute = Image.open(config.program_path + "\\icons\\mute.png")

        self.sound_button_ctk_image_unmute = ctk.CTkImage(dark_image=self.sound_button_image_unmute, size=(32, 32))
        self.sound_button_ctk_image_mute = ctk.CTkImage(dark_image=self.sound_button_image_unmute, size=(32, 32))



        self.sound_button = ctk.CTkButton(self,
                                          image=self.sound_button_ctk_image_unmute,
                                          text="",
                                          fg_color="#000001",
                                          width=32,
                                          height=32,
                                          hover_color="#131F2E",
                                          bg_color="#000001",
                                          anchor="center")
        self.sound_button.place(x=1228, y=4)

        set_opacity(self.sound_button, color="#000001")
        #set_opacity(self.sound_button, color="#131F2E", value=0.5)









        #self.bttm_left_label = ctk.CTkLabel(self, text="", fg_color="#273448", height=65, width=215, corner_radius=32, bg_color="#000001")
        #self.bttm_left_label.place(x=50, y=605)
        #set_opacity(self.bttm_left_label, color="#000001")

    # #0c151d
        #self.bttm_left_label2 = ctk.CTkLabel(self, text="", fg_color="#0c151d", height=52, width=138, corner_radius=32, bg_color="#000001")
        #self.bttm_left_label2.place(x=57, y=611)
        #set_opacity(self.bttm_left_label2, color="#000001")


    def StartMainWindow(self):
        self.mainloop()
    def StopMainWindow(self):
        self.destroy()


class ErrorWindow(ctk.CTk):
    def __init__(self, error_code: str, disable_send_data: bool = False):
        super().__init__()

        font.add_file(program_path + "\\font.ttf")

        self.title("Es ist ein Fehler aufgetreten")
        self.geometry("700x450")
        self.resizable(False, False)
        self.iconbitmap(program_path + "\\icons\\error_icon.ico")

        self.custom_font = ctk.CTkFont("Titillium Web", size=20)

        self.configure(fg_color="#000f0e")


        self.error_window = ctk.CTkTextbox(self, height=410, width=445, border_width=3, bg_color="#000001", fg_color="black", corner_radius=8, text_color="red")
        self.error_window.insert("insert", error_code, tags=None)
        self.error_window.configure(state="disabled")
        self.error_window.place(x=25, y=20)

        self.info_text_label = ctk.CTkTextbox(self,
                                            height=380,
                                            width=200,
                                            border_width=0,
                                            fg_color="#000f0e",
                                            wrap="word",
                                            font=("Titillium Web", 18))
        self.info_text_label.insert("insert", config.error_info_text_box)
        self.info_text_label.configure(state="disabled")
        self.info_text_label.place(x=490, y=20)

        self.ok_button = ctk.CTkButton(self, text="Ok", width=90, height=30, corner_radius=8, fg_color="#000f0e", border_color="white", border_width=2, font=("", 23), command=sys.exit)
        self.ok_button.place(x=600, y=410)


        self.submit_button = ctk.CTkButton(self, text="Senden", width=90, height=30, corner_radius=8, fg_color="#000f0e", border_color="white", border_width=2, font=("", 23), command= lambda: imp_functions.run_contact_tab(config.contact_url + "?error-log=" + error_code))
        self.submit_button.place(x=490, y=410)

        if disable_send_data:
            self.submit_button.place_forget()

        self.bind('<Escape>', lambda e: self.destroy())