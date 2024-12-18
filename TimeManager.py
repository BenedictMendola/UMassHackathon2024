import time


class TimeTracker:
    last_time = time.time()
    deltatime = 0
    startTime = 0

    @staticmethod
    def updateTime():
        current_time = time.time()
        TimeTracker.deltatime = current_time - TimeTracker.last_time
        TimeTracker.last_time = current_time
    @staticmethod
    def timeSinceStart():
        return (time.time() - TimeTracker.startTime)
    def setStartTime():
        TimeTracker.startTime = time.time()
