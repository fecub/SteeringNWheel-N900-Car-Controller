#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importe
import sys
import subprocess, shlex
import os
import signal
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.uic import loadUi


class swheelGUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)  
        # Oberflaeche abbilden:      
        self.ui = loadUi("swheelwindow.ui")
        self.ui.show()
        # Connects
        self.ui.bt_connect.clicked.connect(self.connectHost)
        self.ui.bt_disconnect.clicked.connect(self.disconnectHost)

    def connectHost(self):
        #liest die aktuellen Werte aus den beiden Eingabefeldern aus
        ip = self.ui.lineedit_IP.text()
        # Terminalbefehl
   
        self.launch_Lenkrad  = subprocess.Popen([sys.executable, "/root/coding/Qt-Projects/steeringnwheel/setMouseLenkrad_client.py",  "%s" % ip])
        #self.launch_Lenkrad .communicate()

        self.launch_Tastatur = subprocess.Popen([sys.executable, "/root/coding/Qt-Projects/steeringnwheel/tastatur_client.py",  "%s" % ip])
        #self.launch_Tastatur.communicate()

        self.ui.bt_disconnect.setEnabled(True)
        self.ui.bt_connect.setEnabled(False)
        
        
    def disconnectHost(self):
        os.kill(self.launch_Lenkrad.pid, signal.SIGTERM)
        os.kill(self.launch_Tastatur.pid, signal.SIGTERM)
        self.ui.bt_disconnect.setEnabled(False)
        self.ui.bt_connect.setEnabled(True)

# Starten des Programms
if __name__=="__main__":
    # Qt-Umgebung erzeugen
    app=QApplication(sys.argv)
    # ein Objekt mit dem Namen fenster aus unserer Klasse
    # Minimalbeispiel erzeugen
    fenster=swheelGUI()
    # Programmende
    sys.exit(app.exec_())
