from datetime import date
import json
import linecache

from mailer import Mailer
class Batch:
  def __init__(self,file_path,pattern):
    with open('config.json', 'r') as f:
      config = json.load(f)
      self.file_path=config["file_path"]
      self.pattern=config["pattern"]
      self.email=config["email"]
  def ProcessLog(self):
    fileDate = str(date.today())
    theBody = []
    tmpFile = open(self.file_path)
    for line in tmpFile:
        if self.pattern.lower() in line.lower(): 
          print(line )   
          mailer=Mailer() 
          mailer.sendMail(self.email,"Test",line,"smtp.gmail.com")
    tmpFile.close() 
p1 = Batch("","")
p1.ProcessLog()