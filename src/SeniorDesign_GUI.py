#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:50:18 2017

@author: dellwick
"""

import os
import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.width = 800
        self.height = 480   
        self.init_main_window()
        
    def init_main_window(self):
        main_window = uic.loadUi("../XML/main.ui", self)
        
        # Initialize window itself
        main_window.setFixedSize(self.width, self.height)
        main_window.label_circuit.setPixmap(QtGui.QPixmap("../Images/circuit"))
        self.add_main_functionality(main_window)
        
        # Force load on first pages and tabs
        self.menu_selection_display(0)
        main_window.stacked_widget_start_stop.setCurrentIndex(0)
        self.showFullScreen()

    def add_main_functionality(self, main_window):
        # Initializes widgets
        self.init_help_menu(main_window)
        self.init_stacked_widgets(main_window)
        self.init_combo_box_widgets(main_window)
        self.init_push_buttons(main_window)
        self.init_radio_buttons(main_window)
    
    # help menu located at the top-left of display
    def init_help_menu(self, main_window):
        # application "info" window
        main_window.menu_action_info.triggered.connect(self.init_info_window)
    
    def init_info_window(self):
        info_window = InfoWindow()
        info_window.exec()
        
    def init_push_buttons(self, main_window):
        # Under "Start / Stop"
        main_window.push_button_start.setCheckable(True)
        main_window.push_button_stop.setCheckable(True)
        
        main_window.push_button_start.clicked.connect(lambda: self.push_button_state(main_window))
        main_window.push_button_stop.clicked.connect(lambda: self.push_button_state(main_window))
    
    def init_stacked_widgets(self, main_window):
        # Vertical side menu
        main_window.push_button_start_stop.clicked.connect(lambda: self.menu_selection_display(0))
        main_window.push_button_vnc.clicked.connect(lambda: self.menu_selection_display(1))
        main_window.push_button_settings.clicked.connect(lambda: self.menu_selection_display(2))
       
    def init_combo_box_widgets(self, main_window):
        # Under "Initialize"->"Metal-Oxide-Semiconductor Field-Effect Transistor"
        main_window.comboBox_P1a.addItems(["0", "1", "2", "3", "4", "5"])
        main_window.comboBox_P2a.addItems(["0", "1", "2", "3", "4", "5"])
        main_window.comboBox_P3a.addItems(["0", "1", "2", "3", "4", "5"])
        main_window.comboBox_P1b.addItems(["0", "1", "2", "3", "4", "5"])
        main_window.comboBox_P2b.addItems(["0", "1", "2", "3", "4", "5"])
        main_window.comboBox_P3b.addItems(["0", "1", "2", "3", "4", "5"])
        main_window.comboBox_P1c.addItems(["0", "1", "2", "3", "4", "5"])
    
    def init_radio_buttons(self, main_window):
        # Under "Settings"
        main_window.radio_button_0.setChecked(True)
    
    # For vertical side menu stack selection
    def menu_selection_display(self, i):
        self.stacked_widget_side_menu.setCurrentIndex(i)
        
    def push_button_state(self, main_window):
        if main_window.push_button_start.isChecked():
            main_window.push_button_start.toggle()
            main_window.stacked_widget_start_stop.setCurrentIndex(1)
            self.demo(main_window)
        
        elif main_window.push_button_stop.isChecked():
            main_window.push_button_stop.toggle()
            main_window.stacked_widget_start_stop.setCurrentIndex(0)
            print("***DEMO STOPPED***")

    def demo(self, main_window):
        print("\n***DEMO***")
        
        # Demonstrates checkboxes under "Settings" menu
        check_boxes = [main_window.check_box_0.isChecked(),
                       main_window.check_box_1.isChecked(),
                       main_window.check_box_2.isChecked(),
                       main_window.check_box_3.isChecked(),
                       main_window.check_box_4.isChecked(),
                       main_window.check_box_5.isChecked(),
                       main_window.check_box_6.isChecked(),
                       main_window.check_box_7.isChecked(),
                       main_window.check_box_8.isChecked(),
                       main_window.check_box_9.isChecked()]
        checked = []
        for i in range(len(check_boxes)):
            if check_boxes[i] is True:
                checked.append(i)
        
        # Demonstrates radio buttons under "Settings" menu
        radio_buttons = [main_window.radio_button_0.isChecked(),
                    main_window.radio_button_1.isChecked(),
                    main_window.radio_button_2.isChecked(),
                    main_window.radio_button_3.isChecked()]
        
        radio = []
        for i in range(len(radio_buttons)):
            if radio_buttons[i] is True:
                radio.append(i)
        
        # Demonstrates spin boxes under BJT tab under "Setup" menu
        parameters_BJT = [int(main_window.comboBox_P1a.currentText()),
                          int(main_window.comboBox_P2a.currentText()),
                          int(main_window.comboBox_P3a.currentText())]

        # Demonstrates combo boxes under MOSFET tab under "Setup" menu
        parameters_MOSFET = [int(main_window.comboBox_P1b.currentText()),
                             int(main_window.comboBox_P2b.currentText()),
                             int(main_window.comboBox_P3b.currentText())]
        
        parameters_diode = [int(main_window.comboBox_P1c.currentText())]
        
        # Displays results        
        print("\nCheckboxes marked:")
        print(checked)
        
        print("\nRadio Box marked:")
        print(radio)
                
        print("\nBJT parameters:")
        print(parameters_BJT)
        
        print("\nMOSTFET parameters:")
        print(parameters_MOSFET)
        
        print("\nDiode parameters:")
        print(parameters_diode)
        print()

        
class InfoWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.width = 600
        self.height = 360
        self.init_info_window()
        
    def init_info_window(self):
        info_window = uic.loadUi("../XML/info.ui", self)
        info_window.setFixedSize(self.width, self.height)
        
        info_window.button_box_close.buttons()[0].clicked.connect(self.close)
        
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
