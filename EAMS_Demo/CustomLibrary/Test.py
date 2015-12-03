import xlwt
import xlrd
from xlutils.copy import copy
from xlwt import easyxf
import os
import datetime
from datetime import datetime, date
import time
import wx

global wb

      

def createResultFolder(outputDirectoy):
       count1 = 0
       for root, dirs, files in os.walk(outputDirectoy):
              count1 += len(dirs)
       number = count1+1
       folderName = 'RES' + str(number)       
       newFolderPath = outputDirectoy+"\\" +folderName       
       os.makedirs(newFolderPath)       
       return newFolderPath
  
def popup_show(duration,msg):
       app= wx.App()
       b= wx.BusyInfo(msg)
       time.sleep(duration)
       del b   



      
######  ---  This method creates a new excel fiel with sheet name 'validation'       ###############
       
def create_excel(location):
       LocaitonFolder = createResultFolder(location)
       global ws
       global wb
       global Locaitonfile
       style0 = xlwt.easyxf('font: name Times New Roman, colour blue, bold on')
       wb = xlwt.Workbook()
       ws1 = wb.add_sheet('Summary')
       ws = wb.add_sheet('Validations')
       ws.write(0,0,'STATUS',style0)
       ws.write(0,1,'TEST CASE No',style0)
       ws.write(0,3,'ACTUAL RESULT',style0)
       ws.write(0,2,'EXPECTED RESULT',style0)
       ws.write(0,4,'COMMENTS',style0)
       ws.col(0).width = 6000
       ws.col(1).width = 4000
       ws.col(2).width = 20000
       ws.col(3).width = 20000
       ws.col(4).width = 20000
       loc = LocaitonFolder
       Nfile = "Result.XLS"
       """print loc
       print Nfile"""
       Locaitonfile = loc+"\\"+Nfile
       wb.save(Locaitonfile)

def Telus_Logo_Details(Path,details):
    nl = "\n"    
    tf = open(Path,"a+")    
    tf.writelines(details)
    tf.writelines(nl)
    tf.close

       


def add_result(status1,tc_no1,exp_result1,act_result1,comments1):
       global ws
       global Locaitonfile
       status = status1
       tc_no = tc_no1
       act_result = act_result1
       exp_result = exp_result1
       comment = comments1
       #fail_color = easyxf('pattern: pattern solid, fore_colour red')
       #pass_color = easyxf('pattern: pattern solid, fore_colour green')
       wbR = xlrd.open_workbook(Locaitonfile)
       ws1 = wbR.sheet_by_name('Summary')
       ws = wbR.sheet_by_name('Validations')
       row_count = ws.nrows
       print row_count
       wbW = copy(wbR)
       wbW.get_sheet(1).col(0).width = 6000
       wbW.get_sheet(1).col(1).width = 4000
       wbW.get_sheet(1).col(2).width = 20000
       wbW.get_sheet(1).col(3).width = 20000
       wbW.get_sheet(1).col(4).width = 20000
       wbW.get_sheet(1).write(row_count,0,status)
       wbW.get_sheet(1).write(row_count,1,tc_no)
       wbW.get_sheet(1).write(row_count,2,exp_result)
       wbW.get_sheet(1).write(row_count,3,act_result)
       wbW.get_sheet(1).write(row_count,4,comment)
       wbW.save(Locaitonfile)

       summary(Locaitonfile)
       #Graph(Locaitonfile)

def summary(Locaitonfile):       
       countpass = 0
       countfail = 0
       countpass_1 = 1
       
       #styleTotal = xlwt.easyxf('font: name Times New Roman, colour blue, bold on')
       styleTotal = xlwt.easyxf("pattern: pattern solid, fore_color gray25; font: color black, bold on;")
       styleTotalTC = xlwt.easyxf("pattern: pattern solid, fore_color blue; font: color black, bold on;")
       stylePass = xlwt.easyxf('font: name Times New Roman, colour green, bold on')
       styleFail = xlwt.easyxf('font: name Times New Roman, colour red, bold on')
       stylePass1 = xlwt.easyxf('font: name Times New Roman, colour green, bold off')
       styleFail1 = xlwt.easyxf('font: name Times New Roman, colour red, bold off')
       wb = xlrd.open_workbook(Locaitonfile)
       ws = wb.sheet_by_name('Validations')
       row_count = ws.nrows
       """print row_count-1"""
       for x in range(1, row_count):
              D1 = ws.cell(x,0).value
              if(D1=='PASS'):
                     countpass = countpass+1
              elif(D1!='PASS'):
                     countfail = countfail+1


                   

       #print "PASS COUNT %d" % countpass
       #print "FAIL COUNT %d" % countfail
       wbS = copy(wb)
       wbS.get_sheet(1).col(0).width = 6000
       wbS.get_sheet(1).col(1).width = 4000
       wbS.get_sheet(1).col(2).width = 10000
       wbS.get_sheet(1).col(3).width = 10000
       wbS.get_sheet(1).col(4).width = 10000
       wbS.get_sheet(1).write(0,0,'STATUS',styleTotal)
       wbS.get_sheet(1).write(0,1,'TEST CASE No',styleTotal)
       wbS.get_sheet(1).write(0,2,'EXPECTED RESULT',styleTotal)
       wbS.get_sheet(1).write(0,3,'ACTUAL RESULT',styleTotal)
       wbS.get_sheet(1).write(0,4,'COMMENTS',styleTotal)
       for x in range(1,row_count):
              if(ws.cell(x,0).value=='PASS'):
                     V1=ws.cell(x,0).value
                     V2=ws.cell(x,1).value
                     V3=ws.cell(x,2).value
                     V4=ws.cell(x,3).value
                     V5=ws.cell(x,4).value
                     wbS.get_sheet(1).write(x,0,V1,stylePass1)
                     wbS.get_sheet(1).write(x,1,V2,stylePass1)
                     wbS.get_sheet(1).write(x,2,V3,stylePass1)
                     wbS.get_sheet(1).write(x,3,V4,stylePass1)
                     wbS.get_sheet(1).write(x,4,V5,stylePass1)
              elif(ws.cell(x,0).value!='PASS'):
                     V1=ws.cell(x,0).value
                     V2=ws.cell(x,1).value
                     V3=ws.cell(x,2).value
                     V4=ws.cell(x,3).value
                     V5=ws.cell(x,4).value
                     wbS.get_sheet(1).write(x,0,V1,styleFail1)
                     wbS.get_sheet(1).write(x,1,V2,styleFail1)
                     wbS.get_sheet(1).write(x,2,V3,styleFail1)
                     wbS.get_sheet(1).write(x,3,V4,styleFail1)
                     wbS.get_sheet(1).write(x,4,V5,styleFail1)

       for z in range(1, row_count-1):
              C1 = ws.cell(z,1).value
              C2 = ws.cell(z+1,1).value
              if(C2!=C1):
                     countpass_1 = countpass_1+1
                     
                     
       wbS.get_sheet(0).col(0).width = 5000
       wbS.get_sheet(0).col(1).width = 5000
       wbS.get_sheet(0).write(0,0,'TOTAL COUNT',styleTotal)
       wbS.get_sheet(0).write(1,0,'PASS',stylePass)
       wbS.get_sheet(0).write(2,0,'FAIL',styleFail)
       wbS.get_sheet(0).write(5,0,'Total_TCs',styleTotalTC)
       wbS.get_sheet(0).write(0,1,row_count-1,styleTotal)
       wbS.get_sheet(0).write(1,1,countpass,stylePass)
       wbS.get_sheet(0).write(2,1,countfail,styleFail)
       wbS.get_sheet(0).write(5,1,countpass_1,styleTotalTC)
       wbS.save(Locaitonfile)
       





#=======================================================
# Return all the column data for a specific row in excel
# Arguments : Row_Number , FilePath
# Retrun :  A list variable
#
def readvalueAll(rows,path,sheetName):
       variables = []
       global filelocation
       row = int(rows)
       #filepathlocation = path
       wbR = xlrd.open_workbook(path)
       sh = wbR.sheet_by_name(sheetName)
       row_count = sh.nrows
       print row_count
       cell = sh.cell(0,0)
       for i in range(sh.ncols):
              variables.append(sh.cell_value(row,i))
       return variables

#======================================================

def current_date():
       i = datetime.now()
       print str(i)
       k =  i.strftime('%m/%Y')
       return k


def total_time(d1,d2):
       return(d1-d2)


def time_stamp():
       return(datetime.now())


def current_date_format(format):
      print format
      i = datetime.now()
      print str(i)
      k =  i.strftime(format)
      return k


#========================================================
def Remove_Whitespace(instring):
       return instring.strip()


       
def AppendBANTOFile(BANString):
    nl = "\n"    
    tf = open('C:\EAMS\Output\CreatedBAN.txt',"a+")    
    tf.writelines(BANString)
    tf.writelines(nl)
    tf.close
       
	
if __name__ == "__main__":
       createResultFolder('C:\EAMS\ResultFiles')

def readvalueAllRows(path,sheetName):
       columns = []
       data = []
       global filelocation
       wbR = xlrd.open_workbook(path)
       sh = wbR.sheet_by_name(sheetName)
       num_rows = sh.nrows
       num_cells = sh.ncols - 1
       #print num_rows
       #curr_row = -1
       
       #for i in range(sh.nrows):
              #data.append(sh.row_values(i))        
       return num_rows

def createScreenshotsFolder(outputDirectoy):
       os.makedirs(outputDirectoy)       
       
