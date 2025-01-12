from threading import Thread
from multiprocessing import Process
from imp_functions import mcu_initial_install, play_background_audio
from default_config import sound_activated_after_launcher_start





def MCU_Install_Thread_init(progress_bar_name=None):
    MCU_Install_Thread = Thread(target=lambda: mcu_initial_install(progress_bar_name))
    MCU_Install_Thread.daemon = True
    MCU_Install_Thread.start()
    print("MCU Install Thread started")

class Background_Audio_Thread(Process):
    def __init__(self):
        super().__init__()
        self.name = "Background_Audio_Thread"

    def run(self):
        play_background_audio(play_audio_flag=True)
        print("ssss")
        self.run()

    def kill_background_audio(self):
        self.terminate()