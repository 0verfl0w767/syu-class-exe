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
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(818, 699)
		self.gridLayout = QtWidgets.QGridLayout(Dialog)
		self.gridLayout.setObjectName("gridLayout")
		self.label_2 = QtWidgets.QLabel(Dialog)
		font = QtGui.QFont()
		font.setFamily("맑은 고딕")
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
		self.checkBox_1 = QtWidgets.QCheckBox(Dialog)
		self.checkBox_1.setObjectName("checkBox_1")
		self.gridLayout.addWidget(self.checkBox_1, 1, 1, 1, 1)
		self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
		self.checkBox_2.setObjectName("checkBox_2")
		self.gridLayout.addWidget(self.checkBox_2, 1, 2, 1, 1)
		self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
		self.checkBox_3.setTristate(False)
		self.checkBox_3.setObjectName("checkBox_3")
		self.gridLayout.addWidget(self.checkBox_3, 1, 3, 1, 1)
		self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
		self.checkBox_4.setObjectName("checkBox_4")
		self.gridLayout.addWidget(self.checkBox_4, 1, 4, 1, 1)
		self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
		self.checkBox_5.setObjectName("checkBox_5")
		self.gridLayout.addWidget(self.checkBox_5, 1, 5, 1, 1)
		self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
		self.checkBox_6.setObjectName("checkBox_6")
		self.gridLayout.addWidget(self.checkBox_6, 1, 6, 1, 1)
		self.checkBox_7 = QtWidgets.QCheckBox(Dialog)
		self.checkBox_7.setObjectName("checkBox_7")
		self.gridLayout.addWidget(self.checkBox_7, 1, 7, 1, 1)
		self.checkBox_8 = QtWidgets.QCheckBox(Dialog)
		self.checkBox_8.setObjectName("checkBox_8")
		self.gridLayout.addWidget(self.checkBox_8, 1, 8, 1, 1)
		self.label = QtWidgets.QLabel(Dialog)
		font = QtGui.QFont()
		font.setFamily("맑은 고딕")
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 9)
		self.tableWidget = QtWidgets.QTableWidget(Dialog)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(9)
		self.tableWidget.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(6, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(7, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(8, item)
		self.tableWidget.horizontalHeader().setVisible(True)
		self.tableWidget.horizontalHeader().setHighlightSections(True)
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.verticalHeader().setVisible(True)
		self.tableWidget.verticalHeader().setStretchLastSection(True)
		self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 9)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
	
	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.label_2.setText(_translate("Dialog", "영역"))
		self.checkBox_1.setText(_translate("Dialog", "기초교양"))
		self.checkBox_2.setText(_translate("Dialog", "인성교양"))
		self.checkBox_3.setText(_translate("Dialog", "일반선택영역"))
		self.checkBox_4.setText(_translate("Dialog", "자연과학영역"))
		self.checkBox_5.setText(_translate("Dialog", "사회과학영역"))
		self.checkBox_6.setText(_translate("Dialog", "인문예술영역"))
		self.checkBox_7.setText(_translate("Dialog", "디지털 리터러시영역"))
		self.checkBox_8.setText(_translate("Dialog", "교직영역"))
		self.label.setText(_translate("Dialog", "삼육대학교 공통교양 조회"))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("Dialog", "과목코드"))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("Dialog", "과목명"))
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("Dialog", "학년"))
		item = self.tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("Dialog", "이수구분"))
		item = self.tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("Dialog", "영역구분"))
		item = self.tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("Dialog", "학점"))
		item = self.tableWidget.horizontalHeaderItem(6)
		item.setText(_translate("Dialog", "교수명"))
		item = self.tableWidget.horizontalHeaderItem(7)
		item.setText(_translate("Dialog", "수업시간/장소"))
		item = self.tableWidget.horizontalHeaderItem(8)
		item.setText(_translate("Dialog", "비고"))