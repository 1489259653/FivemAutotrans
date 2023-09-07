from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import re
from transla import trans
from baidu import baidutrans
import time
import random


def qb_dq(txt1):
    orilist = []
    waitlist = []
    n = 0
    txt2 = re.split('"|,|\n', txt1)
    while n <= len(txt2):
        if ((n+1) % 4 == 0):
            orilist.append(txt2[n-3])
            waitlist.append(txt2[n-2])
        n += 1
    return orilist, waitlist


def qb_sq(txt1):
    orilist = []
    waitlist = []
    n = 0
    txt2 = re.split("'|,|\n", txt1)
    while n <= len(txt2):
        if ((n+1) % 4 == 0):
            orilist.append(txt2[n-3])
            waitlist.append(txt2[n-2])
        n += 1
    return orilist, waitlist


def esx_dq(txt1):
    orilist = []
    waitlist = []
    n = 0
    txt2 = re.split('[""]', txt1)

    while n <= len(txt2):
        if ((n+2) % 4 == 0):

            orilist.append(txt2[n-1])
            waitlist.append(txt2[n+1])
        n += 1
    return orilist, waitlist


def esx_sq(txt1):
    orilist = []
    waitlist = []
    n = 0
    txt2 = re.split("['']", txt1)
    while n < len(txt2):

        if ((n+2) % 4 == 0):
            orilist.append(txt2[n-1])
            waitlist.append(txt2[n+1])
        n += 1
    return orilist, waitlist


class UIUI:
    def __init__(self):
        self.ui = QUiLoader().load('myui.ui')
        self.ui.bt1.clicked.connect(self.getstr)
        self.ui.bt2.clicked.connect(self.lt)
        # self.ui.Button_copy.clicked.connect(self.copy_text)

    def getstr(self):  # 与手动创建代码不同，这里需要在（）加入self
        self.ui.textBrowser.clear()
        txt1 = self.ui.textview.toPlainText()
        esqs = self.ui.esx_sq.isChecked()
        edqs = self.ui.esx_dq.isChecked()
        qsqs = self.ui.qb_sq.isChecked()
        qdqs = self.ui.qb_dq.isChecked()
        chins = []
        orilist = []
        waitlist = []
        if qdqs:
            print("qbd", qdqs)
            (orilist, waitlist) = qb_dq(txt1)
            for i in waitlist:
                chins.append(trans(i))
                time.sleep(1+random.random())
            for i, o in zip(chins, orilist):
                self.ui.textBrowser.append(o)
                self.ui.textBrowser.insertPlainText('"')
                self.ui.textBrowser.insertPlainText(i)
                self.ui.textBrowser.insertPlainText('"')
                self.ui.textBrowser.insertPlainText(',')

        else:
            if qsqs:
                print("qbs", qsqs)
                (orilist, waitlist) = qb_sq(txt1)
                for i in waitlist:
                    chins.append(trans(i))
                    time.sleep(1+random.random())
                for i, o in zip(chins, orilist):
                    self.ui.textBrowser.append(o)
                    self.ui.textBrowser.insertPlainText("'")
                    self.ui.textBrowser.insertPlainText(i)
                    self.ui.textBrowser.insertPlainText("'")
                    self.ui.textBrowser.insertPlainText(',')

            else:
                if esqs:
                    print("esxs", txt1)
                    (orilist, waitlist) = esx_sq(txt1)
                    for i in waitlist:
                        chins.append(trans(i))
                        time.sleep(1+random.random())
                    for i, o in zip(chins, orilist):
                        self.ui.textBrowser.append("['")
                        self.ui.textBrowser.insertPlainText(o)
                        self.ui.textBrowser.insertPlainText("'] = '")
                        self.ui.textBrowser.insertPlainText(i)
                        self.ui.textBrowser.insertPlainText("',")

                else:
                    print(txt1)
                    (orilist, waitlist) = esx_dq(txt1)
                    for i in waitlist:
                        chins.append(trans(i))
                        time.sleep(1+random.random())
                    for i, o in zip(chins, orilist):
                        self.ui.textBrowser.append('["')
                        self.ui.textBrowser.insertPlainText(o)
                        self.ui.textBrowser.insertPlainText('"] = "')
                        self.ui.textBrowser.insertPlainText(i)
                        self.ui.textBrowser.insertPlainText('",')
        orilist = []
    # 注意0 4 8 12  1 5 9

    def lt(self):
        info = self.ui.textview.toPlainText()
        self.ui.textBrowser.insertPlainText(trans(info))
        # 与手动创建代码不同，这里需要在（）加入self
        # QMessageBox.about(self.ui, '复制的新窗口', f'{info}')


app = QApplication([])
uiui = UIUI()
uiui.ui.show()
app.exec_()
