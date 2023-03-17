#
#     ____                __________
#    / __ \_   _____  _____/ __/ / __ \_    __
#   / / / / | / / _ \/ ___/ /_/ / / / / | /| / /
#  / /_/ /| |/ /  __/ /  / __/ / /_/ /| |/ |/ /
#  \____/ |___/\___/_/  /_/ /_/\____/ |__/|__/
# 
#  The copyright indication and this authorization indication shall be
#  recorded in all copies or in important parts of the Software.
# 
#  @author 0verfl0w767
#  @link https://github.com/0verfl0w767
#  @license MIT LICENSE
#
import os

from PyQt5 import QtCore, QtWidgets, uic

from ..ui.baseUI import Ui_Dialog

UI_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ui/baseUI.ui"))

form_class = uic.loadUiType(UI_PATH)[0]

class Ui_Dialog_Override(form_class):
  def __init__(self, DATAS):
    self.DATAS = DATAS
    
    self.STATES = {
      "기초교양": False,
      "인성교양": False,
      "일반선택영역": False,
      "자연과학영역": False,
      "사회과학영역": False,
      "인문예술영역": False,
      "디지털 리터러시영역": False,
      "교직영역": False,
    }
  
  def setupUi(self, dialog):
    super().setupUi(dialog)

  def retranslateUi(self, dialog):
    super().retranslateUi(dialog)
    
    dialog.setWindowTitle("syu-class")
    dialog.setWindowFlags(QtCore.Qt.WindowFlags() | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    dialog.resize(818 + 350, 699)
    
    self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
    
    header = self.tableWidget.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
      
    self.checkBox_1.stateChanged.connect(self.checkBox1)
    self.checkBox_2.stateChanged.connect(self.checkBox2)
    self.checkBox_3.stateChanged.connect(self.checkBox3)
    self.checkBox_4.stateChanged.connect(self.checkBox4)
    self.checkBox_5.stateChanged.connect(self.checkBox5)
    self.checkBox_6.stateChanged.connect(self.checkBox6)
    self.checkBox_7.stateChanged.connect(self.checkBox7)
    self.checkBox_8.stateChanged.connect(self.checkBox8)
  
  def stateManage(self, name, value):
    self.tableWidget.setRowCount(0)
    self.STATES[name] = value
    self.tableWidget.setRowCount(300)
    
    count = -1
    
    for state in self.STATES.items():
      if state[1] == False:
        continue
      
      for data in self.DATAS[state[0]]:
        count += 1
        self.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(data["과목코드"]))
        self.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(data["과목명"]))
        self.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(data["학년"]))
        self.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(data["이수구분"]))
        self.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(data["영역구분"]))
        self.tableWidget.setItem(count, 5, QtWidgets.QTableWidgetItem(data["학점"]))
        self.tableWidget.setItem(count, 6, QtWidgets.QTableWidgetItem(data["교수명"]))
        self.tableWidget.setItem(count, 7, QtWidgets.QTableWidgetItem(data["수업시간"]))
        self.tableWidget.setItem(count, 8, QtWidgets.QTableWidgetItem(data["장소"]))
  
  def checkBox1(self, state):
    if state == QtCore.Qt.Checked:
      # print("기초교양 클릭 True")
      self.stateManage("기초교양", True)
    else:
      # print("기초교양 클릭 False")
      self.stateManage("기초교양", False)
  
  def checkBox2(self, state):
    if state == QtCore.Qt.Checked:
      # print("인성교양 클릭 True")
      self.stateManage("인성교양", True)
    else:
      # print("인성교양 클릭 False")
      self.stateManage("인성교양", False)
  
  def checkBox3(self, state):
    if state == QtCore.Qt.Checked:
      # print("일반선택영역 클릭 True")
      self.stateManage("일반선택영역", True)
    else:
      # print("일반선택영역 클릭 False")
      self.stateManage("일반선택영역", False)
  
  def checkBox4(self, state):
    if state == QtCore.Qt.Checked:
      # print("자연과학영역 클릭 True")
      self.stateManage("자연과학영역", True)
    else:
      # print("자연과학영역 클릭 False")
      self.stateManage("자연과학영역", False)
  
  def checkBox5(self, state):
    if state == QtCore.Qt.Checked:
      # print("사회과학영역 클릭 True")
      self.stateManage("사회과학영역", True)
    else:
      # print("사회과학영역 클릭 False")
      self.stateManage("사회과학영역", False)
  
  def checkBox6(self, state):
    if state == QtCore.Qt.Checked:
      # print("인문예술영역 클릭 True")
      self.stateManage("인문예술영역", True)
    else:
      # print("인문예술영역 클릭 False")
      self.stateManage("인문예술영역", False)
  
  def checkBox7(self, state):
    if state == QtCore.Qt.Checked:
      # print("디지털 리터러시영역 클릭 True")
      self.stateManage("디지털 리터러시영역", True)
    else:
      # print("디지털 리터러시영역 클릭 False")
      self.stateManage("디지털 리터러시영역", False)
  
  def checkBox8(self, state):
    if state == QtCore.Qt.Checked:
      # print("교직영역 클릭 True")
      self.stateManage("교직영역", True)
    else:
      # print("교직영역 클릭 False")
      self.stateManage("교직영역", False)