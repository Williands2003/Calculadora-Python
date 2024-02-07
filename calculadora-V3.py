import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.setGeometry(550, 300, 185, 100)
        self.setStyleSheet("background-color: red;")

        self.initUI()

    def initUI(self):
        # Labels
        lb1 = QLabel("1º valor", self)
        lb1.setStyleSheet("color: white;")
        lb1.move(10, 10)

        lb2 = QLabel("2º valor", self)
        lb2.setStyleSheet("color: white;")
        lb2.move(10, 30)

        self.lb3 = QLabel("", self)
        self.lb3.setStyleSheet("color: white;")
        self.lb3.move(10, 70)

        # Caixas de texto
        self.v1 = QLineEdit(self)
        self.v1.setGeometry(70, 10, 100, 20)

        self.v2 = QLineEdit(self)
        self.v2.setGeometry(70, 30, 100, 20)

        # Botões
        self.bt1 = QPushButton("+", self)
        self.bt1.setGeometry(10, 50, 30, 20)
        self.bt1.clicked.connect(self.bt_1)

        self.bt2 = QPushButton("-", self)
        self.bt2.setGeometry(40, 50, 30, 20)
        self.bt2.clicked.connect(self.bt_2)

        self.bt3 = QPushButton("*", self)
        self.bt3.setGeometry(70, 50, 30, 20)
        self.bt3.clicked.connect(self.bt_3)

        self.bt4 = QPushButton("/", self)
        self.bt4.setGeometry(100, 50, 30, 20)
        self.bt4.clicked.connect(self.bt_4)

    def bt_1(self):
        self.lb3.setText(str(float(self.v1.text()) + float(self.v2.text())))

    def bt_2(self):
        self.lb3.setText(str(float(self.v1.text()) - float(self.v2.text())))

    def bt_3(self):
        self.lb3.setText(str(float(self.v1.text()) * float(self.v2.text())))

    def bt_4(self):
        try:
            result = float(self.v1.text()) / float(self.v2.text())
            self.lb3.setText(str(result))
        except ZeroDivisionError:
            self.lb3.setText("Erro: divisão por zero")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    sys.exit(app.exec_())
