import sys
from PyQt4 import QtGui
from Game import Game
from Background import Background

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Game()
    background = Background(window)
    window.setBackground(background)
    window.show()
    sys.exit(app.exec_())