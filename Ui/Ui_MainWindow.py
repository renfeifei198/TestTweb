#! /user/bin/env  python
# -*- coding:utf-8 -*-
# renfeifei
from PyQt5 import QtCore, QtWidgets
from Config.VarConfig import *

"""
主界面的UI
"""

class UiMainWindow(object):
    def initUI(self, main_window):
        """
        生成各个控件
        :return:
        """
        # 主体大小
        main_window.setObjectName('main_window')
        main_window.resize(1000, 650)
        self.widget = QtWidgets.QWidget(main_window)
        self.widget.setGeometry(200, 200, 1000, 650)
        main_window.setWindowTitle('网页自动化脚本')
        main_window.setCentralWidget(self.widget)
        # Label控件
        self.label_stepstable = QtWidgets.QLabel('操作步骤顺序')
        self.label_sheetlist = QtWidgets.QLabel('测试用例')
        self.label_logbrowser = QtWidgets.QLabel('运行日志')
        self.label_executresults = QtWidgets.QLabel('批量执行结果')
        # 按钮控件
        self.btn_execute = QtWidgets.QPushButton('执行编辑中脚本')
        self.btn_savecase = QtWidgets.QPushButton('保存用例->')
        self.btn_addline = QtWidgets.QPushButton('增加一行')
        self.btn_load = QtWidgets.QPushButton('<-读取用例')
        self.btn_executeall = QtWidgets.QPushButton('批量执行')
        # 表格控件
        self.view_stepstable = QtWidgets.QTableWidget()  # 步骤编辑框
        self.view_sheetlist = QtWidgets.QListWidget()  # 用例选择框
        self.view_logbrowser = QtWidgets.QTextBrowser()  # 日志展示框
        self.view_selectedcases = QtWidgets.QListWidget()  # 等待执行用例
        # 下拉框控件
        self.comb_selectexcel = QtWidgets.QComboBox()  # 用例集选择下拉框
        # view_stepstable设置
        self.view_stepstable.setColumnCount(COLUNM_NUMBER)
        self.view_stepstable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 不显示水平滚动条
        self.view_stepstable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # 自适应宽度
        self.view_stepstable.setHorizontalHeaderLabels(COLUNM_NAMES)  # 列名
        # 用例选择支持多选
        self.view_sheetlist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        # 布局框架
        self.box_viewlabels = QtWidgets.QHBoxLayout()  # label布局
        self.box_viewlabels.addWidget(self.label_stepstable)
        self.box_viewlabels.addStretch(1)
        self.box_viewlabels.addWidget(self.label_sheetlist)
        self.box_views = QtWidgets.QHBoxLayout()  # 展示框布局
        self.box_steps = QtWidgets.QVBoxLayout()  # 步骤框布局
        self.box_steps.addWidget(self.view_stepstable)
        self.box_btnsave = QtWidgets.QVBoxLayout()  # 保存读取按钮布局
        self.box_btnsave.addWidget(self.btn_savecase)
        self.box_btnsave.addWidget(self.btn_load)
        self.box_cases = QtWidgets.QVBoxLayout()  # 读取用例布局
        self.box_cases.addWidget(self.comb_selectexcel, stretch = 1)
        self.box_cases.addWidget(self.view_sheetlist, stretch = 2)
        self.box_views.addLayout(self.box_steps, stretch = 8)
        self.box_views.addLayout(self.box_btnsave, stretch = 1)
        self.box_views.addLayout(self.box_cases, stretch = 2)
        self.box_loglabel = QtWidgets.QHBoxLayout()  # 日志labels框布局
        self.box_loglabel.addWidget(self.label_logbrowser)
        self.box_loglabel.addStretch(4)
        self.box_loglabel.addWidget(self.label_executresults)
        self.box_loglabel.addStretch(1)
        self.box_logview = QtWidgets.QHBoxLayout()  # 日志展示框
        self.box_logview.addWidget(self.view_logbrowser, stretch = 8)
        self.box_logview.addWidget(self.view_logbrowser, stretch = 2)
        self.box_logview.addWidget(self.view_selectedcases)
        self.box_executebtns = QtWidgets.QHBoxLayout()  # 执行按钮布局
        self.box_executebtns.addStretch(5)
        self.box_executebtns.addWidget(self.btn_addline)
        self.box_executebtns.addWidget(self.btn_execute)
        self.box_executebtns.addStretch(4)
        self.box_executebtns.addWidget(self.btn_executeall)
        # 布局
        vbox = QtWidgets.QVBoxLayout()  # 最外围垂直框
        vbox.addLayout(self.box_viewlabels)
        vbox.addLayout(self.box_views)
        vbox.addLayout(self.box_loglabel)
        vbox.addLayout(self.box_logview)
        vbox.addLayout(self.box_executebtns)
        self.widget.setLayout(vbox)
