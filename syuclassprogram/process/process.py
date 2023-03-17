#
#     ____                  __________
#    / __ \_   _____  _____/ __/ / __ \_      __
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
import sys

import requests
from PyQt5 import QtWidgets

from ..ui.baseUIManager import Ui_Dialog_Override

class process:
  def __init__(self):
    self.API_DATA = {}
      
    self.DATAS = {}
    self.DATAS["기초교양"] = []
    self.DATAS["인성교양"] = []
    self.DATAS["일반선택영역"] = []
    self.DATAS["자연과학영역"] = []
    self.DATAS["사회과학영역"] = []
    self.DATAS["인문예술영역"] = []
    self.DATAS["디지털 리터러시영역"] = []
    self.DATAS["교직영역"] = []
  
  def request_api(self):
    syu_class_api = requests.get("https://syu-class.kro.kr/api/undergraduate/v1/15")
    self.API_DATA = syu_class_api.json()
  
  def data_remake(self):
    for datas in self.API_DATA["api"]:
      if datas["영역구분"] == "":
        self.DATAS["교직영역"].append(datas)
        continue
      
      self.DATAS[datas["영역구분"]].append(datas)
  
  def sendUI(self):
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_Override(self.DATAS)
    ui.setupUi(dialog)
    ui.checkBox_1.setChecked(True)
    ui.stateManage("기초교양", True)
    dialog.show()
    sys.exit(app.exec_())
  
  def run(self):
    self.request_api()
    self.data_remake()
    self.sendUI()