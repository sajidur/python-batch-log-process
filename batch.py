from datetime import date
import json
import linecache
class Batch:
  def __init__(self,file_path,pattern):
    with open('config.json', 'r') as f:
      config = json.load(f)
      self.file_path=config["file_path"]
      self.pattern=config["pattern"]
  def sendMail(self):
    print("Hello my name is " + self.name)

  def ProcessLog(self):
    fileDate = str(date.today())
    theBody = []
    tmpFile = open(self.file_path)
    for line in tmpFile:
        if self.pattern.lower() in line.lower(): print(line )    
    tmpFile.close() 
p1 = Batch("","")
p1.ProcessLog()