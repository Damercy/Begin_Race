import os
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

import cx_Freeze

executables = [cx_Freeze.Executable("Game.py")]

cx_Freeze.setup( 
        version="1.1",
        name = "The GAME",
        options = {"build_exe":{"packages":["pygame"],
                                "include_files":["car_mod.png","polo_ico.png",
                                                 "bg.wav","Crash.wav"]}},
        executables = executables
        )