class Batch:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sendMail(self):
    print("Hello my name is " + self.name)

  def ProcessLog(self):
    print("Hello my name is " + self.name)

p1 = Batch("John", 36)
p1.sendMail()