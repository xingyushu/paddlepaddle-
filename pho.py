from PyQt4 import QtCore, QtGui
from PyQt4.phonon import *
import sys




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    videofrom = QtGui.QWidget()
    videofrom.setWindowTitle('Video Player')
    videofrom.resize(400,400)
    player = Phonon.VideoPlayer(Phonon.VideoCategory, videofrom)
    player.load(Phonon.MediaSource('aa.mp3'))
    player.play()
    videofrom.show()
    sys.exit(app.exec_())
