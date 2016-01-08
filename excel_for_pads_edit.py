# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 18:44:23 2016

@author: kyle
"""


import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from Pads2Xls import *
import os
import time 
import ImportPads
from pywinauto.application import Application
global m_pads_path
global m_old_pads_path
class ProcessorThread(QThread):
    global m_pads_path
    finishSignal=pyqtSignal(list)
    def __init__(self, parent=None):
        super(ProcessorThread, self).__init__(parent)
    def run(self):
        global m_pads_path
        print 'processorthread run'
        print m_pads_path
        xls_name=m_pads_path.split('.')[0]+'.xls'
        xls_name='kk.xls'
        print xls_name
        pads2xls.GenerateXls(m_pads_path,'kk.xls')
        #time.sleep(6)
        #os.system(xls_name);
        self.me=os.popen(xls_name)
        print 'Thread finish'
        self.finishSignal.emit(['hello,','world','!'])
        
class ExcelToPadsProcessorThread(QThread):
    global m_pads_path
    execl_to_pads_finishSignal=pyqtSignal(list)
    def __init__(self, parent=None):
        super(ExcelToPadsProcessorThread, self).__init__(parent)
    def run(self):
        global m_old_pads_path
        global m_excel_path
        print 'processorthread run'
        print m_excel_path
        print m_old_pads_path
        ImportPads.XlsImportPadsLogic(m_old_pads_path,m_excel_path)
        #time.sleep(6)
        #os.system(xls_name);
        #self.me=os.popen(xls_name)
        print 'Thread finish'
        self.execl_to_pads_finishSignal.emit(['hello,','world','!'])
        
        
qtCreatorFile = "test2.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    pads_path=' '
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.open_pads_file_button.clicked.connect(self.OpenPadsFile4Xls)
        self.excel_generate_button.clicked.connect(self.GenerateExcel)
        self.open_excel_file_button.clicked.connect(self.OpenExcelFile)
        self.open_old_pads_file_button.clicked.connect(self.OpenOldPadsFile)
        self.change_pads_information_button.clicked.connect(self.ChangePadsInformation)      
    def OpenPadsFile4Xls(self):
         self.pads_path=QFileDialog.getOpenFileName(self,"Open file dialog","/","Pads files(*.sch)")  
         self.pads_text.setText(str(self.pads_path))  
         
    def GenerateExcel(self):
        global m_pads_path
        global m_excel_path
        print self.pads_path
        m_pads_path=self.pads_path
        self.excel_generate_button.setText('please wait.....')
        self.excel_generate_button.setDisabled(True)
        self.bwThread = ProcessorThread()
        self.bwThread.finishSignal.connect(self.FinishGenerateExcel)
        #开始执行run()函数里的内容
        self.bwThread.start()
    def FinishGenerateExcel(self):
        self.excel_generate_button.setDisabled(False)
        self.excel_generate_button.setText('Genearte Excel')
        print 'FinishGenerateExcel finish'
        
    def OpenExcelFile(self):
        self.excel_path=QFileDialog.getOpenFileName(self,"Open file dialog","/","Excel files(*.xls)")  
        self.excel_text.setText(str(self.excel_path))  
    def OpenOldPadsFile(self):
        self.old_pads_path=QFileDialog.getOpenFileName(self,"Open file dialog","/","Pads files(*.sch)")  
        self.old_pads_text.setText(str(self.old_pads_path)) 
    def ChangePadsInformation(self):
        global m_old_pads_path   
        global m_excel_path
        m_old_pads_path=self.old_pads_path
        m_excel_path=self.excel_path
        self.change_pads_information_button.setText('please wait.....')
        self.change_pads_information_button.setDisabled(True)
        self.bw2Thread = ExcelToPadsProcessorThread()
        self.bw2Thread.execl_to_pads_finishSignal.connect(self.FinishExcelToPads)
        #开始执行run()函数里的内容
        self.bw2Thread.start()
        
    def FinishExcelToPads(self):
        self.change_pads_information_button.setDisabled(False)
        self.change_pads_information_button.setText('Change Pads')
        print 'FinishGenerateExcel finish'
        
if __name__ == "__main__":
    full_name='C:\PADS Projects\LogicTest.sch'
    xls_name='demo4.xls'
    pads2xls=Pads2Xls()

    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())