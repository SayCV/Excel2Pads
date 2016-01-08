# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 14:16:05 2016

@author: kyle
"""

import win32com.client
import xlrd
def setValue(src,det):
    try:
       det=src
    except:
       det=src    
def XlsImportPadsLogic(pads_file_name,xls_name):
    
    workbook = xlrd.open_workbook(xls_name)
    sheet1=workbook.sheets()[0] 
    print sheet1.nrows;
    name=sheet1.cell(1,1).value
   
    print sheet1.cell(1,1).ctype
    app=win32com.client.Dispatch('PowerLogic.Application')
    app.Visible=True
    powerLogicDoc=app.OpenDocumentNoLock(pads_file_name)
    powerLogicDoc.Components('C2').Attributes.Add('Mfr_Name','kaikai')#('Mfr_Name').Value=sheet1.cell(1,4).value
    for i in range(1,sheet1.nrows-1):
        name=sheet1.cell(i,1).value
        try:
            powerLogicDoc.Components(name).Attributes('Value').Value=sheet1.cell(i,3).value
        except:
            powerLogicDoc.Components(name).Attributes.Add('Value',sheet1.cell(i,3).value)   
        try:
            powerLogicDoc.Components(name).Attributes('Mfr_Name').Value=sheet1.cell(i,4).value
        except:
            powerLogicDoc.Components(name).Attributes.Add('Mfr_Name',sheet1.cell(i,4).value) 
        try:
            powerLogicDoc.Components(name).Attributes('Tolerance').Value=sheet1.cell(i,5).value
        except:
            powerLogicDoc.Components(name).Attributes.Add('Tolerance',sheet1.cell(i,5).value) 

        try:
            powerLogicDoc.Components(name).Attributes('Source_Path').Value=sheet1.cell(i,6).value
        except:
            powerLogicDoc.Components(name).Attributes.Add('Source_Path',sheet1.cell(i,6).value) 

    return
   
#powerLogicDoc.Components[0].Attributes('Value').Value='dfa'
#app.Quit()
   
if __name__ == '__main__':
  full_name='C:\PADS Projects\LogicTest.sch'
  xls_name='demo1.xls'
  XlsImportPadsLogic(full_name,xls_name)