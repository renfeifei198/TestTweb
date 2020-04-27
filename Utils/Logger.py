import datetime
from PyQt5.QtCore import pyqtSignal, QObject


class Logger(QObject):
    trigger = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def logger(self, level, logstr):
        global longmessage
        date = datetime.datetime.now()
        message = r'{} - {} - {}'.format(date, level, logstr)
        if level == 'INFO':
            longmessage = r'<font color="darkgreen">{}</font>'.format(message)
        elif level == 'ERROR':
            longmessage = r'<font color="red">{}</font>'.format(message)
        self.trigger.emit(longmessage)


log = Logger()

if __name__ == '__main__':
    log.logger('info', 'logstr')