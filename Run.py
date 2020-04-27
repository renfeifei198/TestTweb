#! /user/bin/env  python
# -*- coding:utf-8 -*-
# renfeifei
# encoding: utf-8
import sys
from Ui.Ui_MainWindow import UiMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Utils.Logger import log
from Utils.EditExcel import ExcelReader, save_sheet, get_sheet_names
from Utils.GetFuncName import get_func_name
from Utils.ScriptExecute import Worker
from Config.VarConfig import *
"""
处理信号和信号槽函数
"""


class MyWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI(self)
        self.currentexcelname = self.comb_selectexcel.currentText()
        self.currentsheetname = None
        self.testcstepsdata = [] # 传给excel保存的数据
        self.selectedcaseslist = []
        self.assign_excel_combobox()
        self.assign_sheet_list()
        self.connect()

    def connect(self):
        # 按键触发的槽函数
        self.btn_execute.clicked.connect(self.execute_script)
        self.btn_savecase.clicked.connect(self.save_test_case)
        self.btn_addline.clicked.connect(self.add_line)
        self.btn_executeall.clicked.connect(self.execute_all)
        # 选中触发的槽函数
        self.comb_selectexcel.currentIndexChanged.connect(self.assign_sheet_list)
        self.btn_load.clicked.connect(self.load_sheet)
        self.view_sheetlist.itemClicked.connect(self.item_click)
        # 自定义信号槽
        log.trigger.connect(self.printf)

    def printf(self, msg):
        self.view_logbrowser.append(msg)  # 在指定的区域显示提示信息
        cursor = self.view_logbrowser.textCursor()
        self.view_logbrowser.moveCursor(cursor.End)  # 光标移到最后，这样就会自动显示出来
        QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def add_line(self):
        row = self.view_stepstable.rowCount()
        log.logger("INFO", '行数为:{}'.format(row+1))
        self.view_stepstable.setRowCount(row + 1)

    def assign_excel_combobox(self):
        excelnames = ExcelReader.get_file_list()
        if excelnames:
            self.comb_selectexcel.addItems(excelnames)
        else:
            self.comb_selectexcel.addItem('未发现EXCEL')

    def assign_sheet_list(self):
        self.view_sheetlist.clear()
        self.currentexcelname = self.comb_selectexcel.currentText()
        sheetnames = get_sheet_names(self.currentexcelname)
        self.view_sheetlist.addItems(sheetnames)
        log.logger("INFO", '目前选中的excel是:{}'.format(self.currentexcelname))

    def execute_script(self):
        self.testcstepsdata = []
        self.get_stpes_data()
        self.funclist = get_func_name(self.testcstepsdata)
        self.slave = Worker(self.funclist)
        self.slave.start()

    def save_test_case(self):
        self.get_stpes_data()
        save_sheet(self.currentexcelname, self.currentsheetname, self.testcstepsdata)

    def load_sheet(self):
        log.logger('INFO', '目前的excelname:{}'.format(self.currentexcelname))
        log.logger('INFO', '目前的sheetname:{}'.format(self.currentsheetname))
        self.testcstepsdata = ExcelReader.get_sheet_value(self.currentexcelname, self.currentsheetname)
        if self.testcstepsdata == None :
            log.logger('INFO', '选中sheet为空')
        else:
            row = len(self.testcstepsdata)
            self.view_stepstable.setRowCount(row)
            for i in range(0, row):
                for col in range(0, len(self.testcstepsdata[i])):
                    temp = QTableWidgetItem(str(self.testcstepsdata[i][col]))
                    self.view_stepstable.setItem(i, col, temp)

    def item_click(self):
        self.selectedcaseslist = []
        self.currentsheetname = self.view_sheetlist.currentItem().text()
        for i in self.view_sheetlist.selectedItems():
            self.selectedcaseslist.append(i.text())
        log.logger('INFO', '目前选中的用例为:{}'.format(self.currentsheetname))

    def execute_all(self):
        log.logger('INFO','选中的sheename为:{}'.format(self.selectedcaseslist))

    def get_stpes_data(self):
        row = self.view_stepstable.rowCount()
        self.testcstepsdata = []
        for item in range(0, row):
            testdict = []
            for i in range(1, 6):
                try:
                    temp = self.view_stepstable.item(item, i - 1)
                    if temp:
                        testdict.append(temp.text())
                    else:
                        testdict.append('NA')
                except Exception as e:
                    log.logger('ERROR', e)
            self.testcstepsdata.append(testdict.copy()) # 获取需要保存的steps数据
        print(self.testcstepsdata)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mytest = MyWindow()
    mytest.show()
    sys.exit(app.exec_())