import pywinstyles

from gui import MainRunWindow, ErrorWindow, FirstRunWindow
from imp_functions import CreateMBox, retrieve_config_argument_to_file, add_config_argument_to_file
from default_config import program_path, mcu_appdata, mc_folder, fully_installed_file, \
    sound_activated_after_launcher_start, custom_config_file
from threads import MCU_Install_Thread_init, Background_Audio_Thread
from multiprocessing import freeze_support

import sys
import os
import platform
import time
import traceback
#import pyuac

FRW_class = None
MRW_class = None
EW_class = None


#if not pyuac.isUserAdmin():
#    pyuac.runAsAdmin()
#else:
#    pass



class NoOSSupport(Exception):
    pass

if not sys.argv[1] == "--dev":
    def error_handler(exc_type, exc_value, exc_traceback):
        global EW_class
        error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        print("Error Handler gestartet")
        if exc_type == NoOSSupport:
            EW_class = ErrorWindow(error_code=error_message, disable_send_data=True)
            EW_class.mainloop()
        else:
            EW_class = ErrorWindow(error_code=error_message)
            EW_class.mainloop()
        exit(0)


    sys.excepthook = error_handler

system_tag = platform.system()
if system_tag != "Windows":
    raise NoOSSupport("Dieses Programm unterstützt ihr Betriebssystem nicht:", system_tag)


def launcher_firt_time_run():
    global FRW_class
    FRW_class = FirstRunWindow()

    MCU_Install_Thread_init(FRW_class.install_progressbar)

    FRW_class.fade_in()
    FRW_class.StartFirstWindow()
    print("test")



if __name__ == "__main__":
    freeze_support()


    if os.path.isfile(fully_installed_file):
        pass
    else:

        #Background_Audio_Thread().__init__()

        MRW_class = MainRunWindow()

        pywinstyles.change_header_color(MRW_class, "#141E28")
        MRW_class.StartMainWindow()



        #launcher_firt_time_run()
