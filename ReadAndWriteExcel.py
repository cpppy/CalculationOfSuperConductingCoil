# -*- coding: cp936 -*-
# read and write excel file

'''
#build excel and write into data
import xlwt
file = xlwt.Workbook()
table = file.add_sheet('Sheet1', cell_overwrite_ok=True)
table.write(1,1,'test')

file.save('demo.xls')

'''


'''
�ο�����
import xlwt
�½�һ��excel�ļ�
file = xlwt.Workbook() #ע�������Workbook����ĸ�Ǵ�д�������
�½�һ��sheet
table = file.add_sheet('sheet name')
д������table.write(��,��,value)
table.write(0,0,'test')
�����һ����Ԫ���ظ�������������
returns error:# Exception: Attempt to overwrite cell:# sheetname=u'sheet 1' rowx=0 colx=0
�����ڴ�ʱ��cell_overwrite_ok=True���
table = file.add_sheet('sheet name',cell_overwrite_ok=True)
�����ļ�
file.save('demo.xls')
���⣬ʹ��style
style = xlwt.XFStyle() #��ʼ����ʽ
font = xlwt.Font() #Ϊ��ʽ��������
font.name = 'Times New Roman'
font.bold = True
style.font = font #Ϊ��ʽ��������
table.write(0, 0, 'some bold Times text', style) # ʹ����ʽ
xlwt ����Ԫ��������е����ø�ʽ����������������Լ���ʽ�������Ķ�Դ���룬���������ӣ�
dates.py, չʾ������ò�ͬ�����ݸ�ʽ
hyperlinks.py, չʾ��δ��������� (hint: you need to use a formula)
merged.py, չʾ��κϲ�����
row_styles.py, չʾ���Ӧ��Style�����и�����. 


#read and write excel file
import xlrd
import xlwt
filename = "demo.xls"
book = xlrd.open_workbook(filename)
shxrange = range(book.nsheets)
try:
    sh=book.sheet_by_name("newsheet")
except:
    print "no sheet in %s named sheet" %filename

nrows = sh.nrows
ncols = sh.ncols
print "nrows %d, ncols %d" %(nrows,ncols)
print '\n'
cell_value = sh.cell_value(1,1)
print cell_value 

'''

#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import wx
import os
from win32com.client import Dispatch 
import win32com.client
import time

i=123456

class easyExcel: 
    """A utility to make it easier to get at Excel.  Remembering 
    to save the data is your problem, as is  error handling. 
    Operates on one workbook at a time.""" 
    def __init__(self, filename=None): 
        self.xlApp = win32com.client.Dispatch('Excel.Application') 
        if filename: 
            self.filename = filename 
            self.xlBook = self.xlApp.Workbooks.Open(filename) 
        else: 
            self.xlBook = self.xlApp.Workbooks.Add() 
            self.filename = ''  
    def save(self, newfilename=None): 
        if newfilename: 
            self.filename = newfilename 
            self.xlBook.SaveAs(newfilename) 
        else: 
            self.xlBook.Save()    
    def close(self): 
        self.xlBook.Close(SaveChanges=0) 
        del self.xlApp 
    def getCell(self, sheet, row, col): 
        "Get value of one cell" 
        sht = self.xlBook.Worksheets(sheet) 
        return sht.Cells(row, col).Value 
    def setCell(self, sheet, row, col, value): 
        "set value of one cell" 
        sht = self.xlBook.Worksheets(sheet) 
        sht.Cells(row, col).Value = value 
    def getRange(self, sheet, row1, col1, row2, col2): 
        "return a 2d array (i.e. tuple of tuples)" 
        sht = self.xlBook.Worksheets(sheet) 
        return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value 
    def addPicture(self, sheet, pictureName, Left, Top, Width, Height): 
        "Insert a picture in sheet" 
        sht = self.xlBook.Worksheets(sheet) 
        sht.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height) 
    def cpSheet(self, before): 
        "copy sheet" 
        shts = self.xlBook.Worksheets 
        shts(1).Copy(None,shts(1)) 



if __name__ == "__main__": 
    #PNFILE = r'c:\screenshot.bmp' 
    xls = easyExcel(r'C:/Python27/HEPAK Example.xls') 
    #xls.addPicture('Sheet1', PNFILE, 20,20,1000,1000) 
    #xls.cpSheet('Sheet1')
    print xls.getCell(1,9,3)
    print xls.getCell(1,20,4)
    print xls.getCell(1,21,4)

    xls.setCell(1,9,3,i)
    print xls.getCell(1,9,3),'\t',xls.getCell(1,20,4),'\t',xls.getCell(1,21,4)

    xls.setCell(1,9,3,2*i)
    print xls.getCell(1,9,3),'\t',xls.getCell(1,20,4),'\t',xls.getCell(1,21,4)

    attempts =0
    success = False
    for j in range(10000):
        #time.sleep(1)
        try:
            xls.setCell(1,9,3,i+20*j)
            print xls.getCell(1,9,3),'\t',xls.getCell(1,20,4),'\t',xls.getCell(1,21,4)
        except:
            xls.setCell(1,9,3,i+20*(j-1))
            print xls.getCell(1,9,3),'\t',xls.getCell(1,20,4),'\t',xls.getCell(1,21,4)
            print "fail to get value in p= %f" %(i+20*j)
    xls.close()

'''
    #��������button
    class myapp(wx.App):
                        def OnInit(self):
                                frame=wx.Frame(parent=None,
                                                                id=-1,
                                             title='BUTTON',
                                    pos=(100,100),
                                    size=(800,880),
                                    style=wx.DEFAULT_FRAME_STYLE,
                                    name="framebutton")
                        
                                panel=wx.Panel(frame,-1)
                        
                                self.button1=wx.Button(panel,
                                                                -1,
                                                                'Button1',
                                                                 pos=(500,500),
                                                                size=(200,200)
                                                              )
                                self.Bind(wx.EVT_BUTTON,self.OnButton1,self.button1)
                        
                                self.button2=wx.Button(panel,
                                                                -1,
                                                                'Button2',
                                                                 pos=(100,500),
                                                                size=(200,200)
                                                              )
                                self.Bind(wx.EVT_BUTTON,self.OnButton2,self.button2)
                                self.button1.SetDefault()

                                #self.label=wx.StaticText(panel,-1,'vhjkbkl',pos=(200,200))

                        
                                frame.Show()
                                return True

                        def OnButton1(self,event):
                                self.button2.SetLabel('Button1')
                                self.button2.SetDefault()
                                self.button1.SetLabel('Button2')

                        def OnButton2(self,event):
                                self.button1.SetLabel('Button1')
                                self.button1.SetDefault()
                                self.button2.SetLabel('Button2')        
                                                              
                        
    app=myapp()
    app.MainLoop()
    '''





























