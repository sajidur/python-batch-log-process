from datetime import date
import linecache
class Batch:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sendMail(self):
    print("Hello my name is " + self.name)

  def ProcessLog(self):
    fileDate = str(date.today())
    theBody = []
    tmpFile = open(r'C:\My data\Guru Project\python-batch-log-process\samplelog.log')
    for line in tmpFile:
        if 'Error' in line: print(line )    
    tmpFile.close() 
p1 = Batch("John", 36)
p1.ProcessLog()