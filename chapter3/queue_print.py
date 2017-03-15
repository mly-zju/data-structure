from queue import Queue
import random


class Task:
    def __init__(self, time):
        self.time = time
        self.pageNum = random.randrange(1, 21)

    def setPageNum(self, num):
        self.pageNum = num

    def getPageNum(self):
        return self.pageNum

    def getWaitTime(self, time):
        return time - self.time


class Printer:
    def __init__(self, ppm):
        self.ppm = ppm
        self.timeRemaining = 0
        self.currentTask = None

    def isBusy(self):
        return self.timeRemaining > 0

    def handling(self):
        self.timeRemaining = self.timeRemaining - 1

    def startNext(self, task):
        self.currentTask = task
        self.timeRemaining = task.getPageNum() * 60 / self.ppm
        self.handling()


if __name__ == '__main__':
    printer = Printer(10)
    taskQ = Queue()
    currentTime = 0
    taskNum = 20
    end = False
    waitTime = 0
    while not end:
        currentTime = currentTime + 1
        if taskNum > 0:
            if(random.randrange(0, 180) == 0):
                taskQ.enqueue(Task(currentTime))
                taskNum = taskNum - 1
        if taskNum == 0 and taskQ.isEmpty():
            end = True
        else:
            if (not printer.isBusy()) and (not taskQ.isEmpty()):
                print('push new task')
                currentTask = taskQ.dequeue()
                waitTime = waitTime + currentTask.getWaitTime(currentTime)
                printer.startNext(currentTask)
            else:
                printer.handling()

    avergeWaitTime = waitTime / 20
    print(avergeWaitTime)
