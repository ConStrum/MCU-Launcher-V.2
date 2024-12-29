from threading import Thread
from multiprocessing import Process, freeze_support
from imp_functions import mcu_initial_install, play_background_audio





def MCU_Install_Thread_init(progress_bar_name=None):
    MCU_Install_Thread = Thread(target=lambda: mcu_initial_install(progress_bar_name))
    MCU_Install_Thread.daemon = True
    MCU_Install_Thread.start()
    print("MCU Install Thread started")


def Background_Audio_Thread_init():
    Background_Audio_Thread = Process(target=play_background_audio)
    Background_Audio_Thread.daemon = True
    Background_Audio_Thread.start()
    print("Background Audio Thread started")