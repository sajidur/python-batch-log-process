from datetime import date
import json
import linecache

from mailer import Mailer
class Batch:
  def __init__(self):
    with open('config.json', 'r') as f:
      config = json.load(f)
      self.file_path=config["file_path"]
      self.pattern=config["pattern"]
      self.email=config["email"]
  def ProcessLog(self):
    fileDate = str(date.today())
    theBody = []
    print(self.file_path+""+fileDate)
    tmpFile = open(self.file_path)
    for line in tmpFile:
        if self.pattern.lower() in line.lower(): 
          print(line )   
          mailer=Mailer() 
         # mailer.send("sajid.ict@hotmail.com",line)
    tmpFile.close() 
