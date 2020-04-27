#! /user/bin/env  python
# -*- coding:utf-8 -*-
# renfeifei
import os

# 项目根目录
PROJECTPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# chrome驱动目录
CHROMEPATH = PROJECTPATH + f'\drivers\chromedriver.exe'
# excel文件路径
EXCELPATH = PROJECTPATH + r'\scripts'
# 步骤编辑框列名
COLUNM_NAMES = ['操作名称', '关键字', '定位方式', '操作对象', '输入的值']
# 步骤编辑框列数
COLUNM_NUMBER = 5
# 截图路径
EXCEPTPATH = PROJECTPATH + r'\screenshots'
# 字段
DICTKEYS = ['testStepDescribe', 'keyWord', 'elementBy', 'elementLocator', 'operateValue']