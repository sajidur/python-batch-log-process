from batch import Batch


import sched
import time

while True:
    p1 = Batch()
    p1.ProcessLog()
    time.sleep(30)
