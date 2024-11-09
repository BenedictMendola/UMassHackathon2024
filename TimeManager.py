import time

class TimeTracker:
    deltatime = 0
    oldTime = -.01

    def updateTime():
        TimeTracker.deltatime = time.time() -TimeTracker.oldTime
        TimeTracker.oldTime = time.time()