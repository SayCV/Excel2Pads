# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 14:16:05 2016

@author: kyle
"""

import win32com.client
import xlwt
import argparse

class Pads2Xls:
    def GenerateXls(self,pads_file_name,xls_name, verbose):
        if verbose:
            print('pads_file_name', pads_file_name)
            print('xls_name', xls_name)
        f=xlwt.Workbook()
        sheet1=f.add_sheet("autog",cell_overwrite_ok=True)
        row0=[u'Item',u'Name',u'PCB DECAL',u'Value',u'Mfr_Name',u'Tolerance',u'SourcePath'];
        for i in range(0,len(row0)):
            sheet1.write(0,i,row0[i]);


        app=win32com.client.Dispatch('PowerLogic.Application')
        app.Visible=True
        powerLogicDoc=app.OpenDocumentNoLock(pads_file_name)
        print (powerLogicDoc)
        parts=powerLogicDoc.PartTypes

        components=powerLogicDoc.Components
        i=1
        for component in components:
            attributes=component.Attributes
            sheet1.write(i,0,str(i-1))
            sheet1.write(i,1,component.Name)
            sheet1.write(i,2,component.PCBDecal)
            sheet1.write(i,3,str(attributes('Value')))
            sheet1.write(i,4,str(attributes('Mfr_Name')))
            sheet1.write(i,5,str(attributes('Tolerance')))
            sheet1.write(i,6,str(attributes('Source_Path')))
            i=i+1
        f.save(xls_name)
        
        #app2 = win32com.client.Dispatch('Excel.Application')
        #app2.Visible=True
        #app2.Workbooks.Open(xls_name)
#powerLogicDoc.Components[0].Attributes('Value').Value='dfa'
#app.Quit()
   
if __name__ == '__main__':
  full_name='C:\PADS Projects\LogicTest.sch'
  xls_name='G:demo9.xls'
  pads2xls=Pads2Xls()
  pads2xls.GenerateXls(full_name,xls_name, verbose=True)