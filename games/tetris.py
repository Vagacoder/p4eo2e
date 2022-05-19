import os
import sys
import random
# from pandas import *

# ! need install the library of modules, run: pip install modules
from modules import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class TetrisGame(QMainWindow):
    def __init__(self, parent=None):
        super(TetrisGame, self).__init__(parent)
        self.is_paused = False
        self.is_started = False
        self.initUI()


    def initUI(self):
        # * icon
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'resouces/icon.jpg')))

        # * grid size
        self.grid_size = 22

        # * fps
        self.fps = 200
        self.timer = QBasicTimer()

        # * focus
        self.setFocusPolicy(Qt.StrongFocus)

        # * horizontal layout
        layout_horizontal = QHBoxLayout()
        self.inner_board = InnerBoard()
