from PyQt5.QtCore import QThread, pyqtSignal
from PageAction.PageAction import *
from Utils.Logger import log

class Worker(QThread):
    def __init__(self, teststeplist):
        super(QThread, self).__init__()
        self.teststeplist = teststeplist

    def run(self):
        for index in range(0, len(self.teststeplist)):
            try:
                eval(self.teststeplist[index])
            except Exception as e:
                log.logger('ERROR', '执行语句错误，错误语句为{}:{}'.format(self.teststeplist[index], e))

    def kill_thread(self):
        self.terminate()