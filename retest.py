#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Frist PyQt5 program
'''
__author__ = 'jack'

from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QHBoxLayout,QPushButton,QLineEdit,QTextEdit,QVBoxLayout,QMessageBox
import sys
import requests
import time

class ShowWindow(QWidget):

    def __init__(self):
        super(ShowWindow,self).__init__()      
        self.initUI()
        self.resize(800,600)


    def initUI(self):
        self.inputLabel = QLabel("输入URL")
        self.editText = QTextEdit()
        self.refreshButton = QPushButton("开始测试")

        self.refreshButton.clicked.connect(self.refreshText)

#标签和输入框横向布局
        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.editText)

#按钮横向布局
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.refreshButton)

#主窗口竖向布局
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle('浏览请求测试') 
        self.show()

    
#定义点击按钮就开始刷新        
    def refreshText(self):
        text = self.editText.toPlainText #多行输入的文本赋值给text
        if text == '':
            QMessageBox.information(self, "空文本",
                                    "请输入网址")  #文本为空的提示
        else :
            to_oneline = ' '.join(text.split())  #多行的text转换成单行
            URL_LIST = to_oneline.split(' ') #单行数据转为列表数据
            url_num = len(URL_LIST)
            print("网址有：",url_num,"个")        
        
            for i in range(2):
                print('------',i,'------')
                for j in range(url_num):
                    url = URL_LIST[j]
                    requests.get(url)
                    time.sleep(3)
                    print(j)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowWindow()
    sys.exit(app.exec_())
