from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_1.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.pbt_1.setObjectName("pbt_1")
        self.pbt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_2.setGeometry(QtCore.QRect(90, 50, 121, 31))
        self.pbt_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pbt_2.setAcceptDrops(False)
        self.pbt_2.setAutoFillBackground(False)
        self.pbt_2.setCheckable(False)
        self.pbt_2.setAutoRepeat(False)
        self.pbt_2.setAutoExclusive(False)
        self.pbt_2.setObjectName("pbt_2")
        self.pbt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_3.setGeometry(QtCore.QRect(220, 50, 71, 31))
        self.pbt_3.setObjectName("pbt_3")
        self.pbt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_4.setGeometry(QtCore.QRect(300, 50, 111, 31))
        self.pbt_4.setObjectName("pbt_4")
        self.pbt_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_5.setGeometry(QtCore.QRect(420, 50, 71, 31))
        self.pbt_5.setObjectName("pbt_5")
        self.listWidget_1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_1.setGeometry(QtCore.QRect(10, 90, 481, 311))
        self.listWidget_1.setObjectName("listWidget_1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 481, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Обращение к функции реализации нажатий клавиш
        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbt_1.setText(_translate("MainWindow", "Архив"))
        self.pbt_2.setText(_translate("MainWindow", "Добавить данные"))
        self.pbt_3.setText(_translate("MainWindow", "Поиск по ФИ"))
        self.pbt_4.setText(_translate("MainWindow", "Изменить номер"))
        self.pbt_5.setText(_translate("MainWindow", "Удалить"))

        # функция реализации нажатий клавиш
    def add_function(self):
        self.text = ""
        self.lineEdit.setPlaceholderText("Введите текст") # Плейсхолдер
        # выводим весь текст из файла
        self.pbt_1.clicked.connect(lambda: self.write_label(self.text))

        # Вводи нового текста в файл
        self.pbt_2.clicked.connect(lambda: self.onChanged(self.lineEdit.text()))  # извлекаю данные из Строчки и
        # передаю их

        # Поиск номера телефона по имени
        self.pbt_3.clicked.connect(lambda: self.toFind(self.lineEdit.text()))

        # Изменить номер телефона по имени
        self.pbt_4.clicked.connect(lambda: self.change_number(self.lineEdit.text()))

        # Удаление пользователя
        self.pbt_5.clicked.connect(lambda: self.delele_user(self.lineEdit.text()))

        # Динамическое отслеживание введенного текст
        # self.lineEdit.textChanged[str].connect(self.onChanged)

    # Функция вывода на экран всех пользователей
    def write_label(self, text):
        self.listWidget_1.addItem(f"{text}")
        with open("test.txt", "r", encoding="UTF-8") as self.file1:
            self.fl = self.file1.readlines()
            for i in self.fl:
                # выводим информацию на экран
                self.str0 = i.split(";")
                self.str1 = self.str0[0]
                self.str2 = self.str0[1]
                self.listWidget_1.addItem(f"{self.str1} | {self.str2}")

    # Функция добавления нового пользователя
    def onChanged(self, text):
        with open("test.txt", "a", encoding="UTF-8") as self.file1:
            self.file1.write(text + "\n")

    # Функция поиска номера телефона по имени и вывод его на экран
    def toFind(self, text):
        with open("test.txt", "r", encoding="UTF-8") as self.file1:
            self.fl = self.file1.readlines()
            for i in self.fl:
                # выводим информацию на экран
                self.str0 = i.split(";")
                self.str1 = self.str0[0]
                self.str2 = self.str0[1]
                if self.str1 == text:
                    self.listWidget_1.addItem(f"{self.str2}")

    # функция изменения номера телефона
    def change_number(self, text1):
        self.text = text1.split(";")
        open("test1.txt", "w").close()
        with open("test.txt", "r", encoding="UTF-8") as self.file1, open("test1.txt", "a",
                                                                         encoding="UTF-8") as self.file2:
            self.fl = self.file1.readlines()
            for i in self.fl:
                self.str1 = i.split(";")
                if self.str1[0] == self.text[0]:
                    self.file2.writelines(f"{self.str1[0]};{self.text[1]}\n")
                else:
                    self.file2.writelines(i)
        open("test.txt", "w").close()
        with open("test.txt", "r+", encoding="UTF-8") as file1, open("test1.txt", "r", encoding="UTF-8") as file2:
            fl = file2.readlines()
            for i in fl:
                file1.writelines(i)  # заполняю старый файл новыми данными

    def delele_user(self, text1):
        self.text = text1.split(";")
        open("test1.txt", "w").close()
        with open("test.txt", "r", encoding="UTF-8") as self.file1, open("test1.txt", "a",
                                                                         encoding="UTF-8") as self.file2:
            self.fl = self.file1.readlines()
            for i in self.fl:
                self.str1 = i.split(";")
                if self.str1[0] == self.text[0]:
                    continue
                else:
                    self.file2.writelines(i)
        open("test.txt", "w").close()
        with open("test.txt", "r+", encoding="UTF-8") as file1, open("test1.txt", "r", encoding="UTF-8") as file2:
            fl = file2.readlines()
            for i in fl:
                file1.writelines(i)  # заполняю старый файл новыми данными


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
