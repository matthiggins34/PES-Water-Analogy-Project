#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:50:18 2017

@author: dellwick
"""

import os
import sys
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.window_icon = QIcon("../Images/nutty")
        self.width = 800
        self.height = 480   
        self.init_main_window()
        
    def init_main_window(self):
        main_window = uic.loadUi("../XML/main.ui", self)
        self.setWindowIcon(self.window_icon)
        main_window.setFixedSize(self.width, self.height)
        
        self.command_help_menu(main_window)
        
        self.init_stacked_widget(main_window)
        
        self.add_main_functionality(main_window)
        
        self.showFullScreen()

    def command_help_menu(self, main_window):
        # application info window
        main_window.action_about.setStatusTip("System Help")
        main_window.action_about.triggered.connect(self.init_info_window)
    
    def init_info_window(self):
        info_window = InfoWindow()
        info_window.exec()
        
    def init_stacked_widget(self, main_window):
        # commented out lines display text when hovered over with cursor
        
        #main_window.button_start_stop.setStatusTip("Start / Stop")
        #main_window.button_initialize.setStatusTip("Initialize")
        #main_window.button_vnc.setStatusTip("Initialize")
        #main_window.button_settings.setStatusTip("Initialize")

        # Vertical side menu
        main_window.button_initialize.clicked.connect(lambda: self.display(0))        
        main_window.button_start_stop.clicked.connect(lambda: self.display(1))
        main_window.button_vnc.clicked.connect(lambda: self.display(2))
        main_window.button_settings.clicked.connect(lambda: self.display(3))
        
    # For vertical side menu stack selection
    def display(self, i):
        self.stacked_widget.setCurrentIndex(i)

    def add_main_functionality(self, main_window):
        
        # Start/Stop buttons: apply and cancel respectively
        main_window.button_box_start_stop.buttons()[1].clicked.connect(lambda: self.demo(main_window))
        main_window.button_box_start_stop.buttons()[0].clicked.connect(lambda: sys.exit())
    
    def demo(self, main_window):
        print("\n***DEMO***")
        checkBoxes = [main_window.checkBox_0.isChecked(),
                      main_window.checkBox_1.isChecked(),
                      main_window.checkBox_2.isChecked(),
                      main_window.checkBox_3.isChecked(),
                      main_window.checkBox_4.isChecked(),
                      main_window.checkBox_5.isChecked(),
                      main_window.checkBox_6.isChecked(),
                      main_window.checkBox_7.isChecked(),
                      main_window.checkBox_8.isChecked(),
                      main_window.checkBox_9.isChecked(),
                      main_window.checkBox_10.isChecked(),
                      main_window.checkBox_11.isChecked()] 
        checked = []
        
        parameters_BJT = [main_window.spinBox_BJT_0.value(),
                         main_window.spinBox_BJT_1.value(),
                         main_window.spinBox_BJT_2.value()]               
        
        parameters_MOSFET = [main_window.spinBox_MOSFET_0.value(),
                            main_window.spinBox_MOSFET_1.value(),
                            main_window.spinBox_MOSFET_2.value()]

        main_window.P1a.setText("P1 = " + str(int(round(main_window.spinBox_BJT_0.value()))))
        main_window.P2a.setText("P2 = " + str(int(round(main_window.spinBox_BJT_1.value()))))
        main_window.P3a.setText("P3 = " + str(int(round(main_window.spinBox_BJT_2.value()))))

        main_window.P1b.setText("P1 = " + str(int(round(main_window.spinBox_MOSFET_0.value()))))
        main_window.P2b.setText("P2 = " + str(int(round(main_window.spinBox_MOSFET_1.value()))))
        main_window.P3b.setText("P3 = " + str(int(round(main_window.spinBox_MOSFET_2.value()))))
        for i in range(len(checkBoxes)):
            if checkBoxes[i] is True:
                checked.append(i)
                
        print("\nCheckboxes marked:")
        print(checked)
                
        print("\nBJT parameters:")
        print(parameters_BJT)
        
        print("\nMOSTFET parameters:")
        print(parameters_MOSFET)
        print()
        
class InfoWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.window_icon = QIcon("../Images/nutty")
        self.width = 600
        self.height = 360
        self.init_info_window()
        
    def init_info_window(self):
        info_window = uic.loadUi("../XML/info.ui", self)
        self.setWindowIcon(self.window_icon)
        info_window.setFixedSize(self.width, self.height)
        
        info_window.button_box_close.buttons()[0].clicked.connect(self.close)
        
        self.show()
    
def main():
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
