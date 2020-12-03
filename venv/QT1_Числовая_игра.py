import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel



class Example(QWidget):
    def __init__(self):
        self.x = random.randint(10, 30)
        self.y = random.randint(2, 10)
        self.z = random.randint(2, 10)

        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 100, 300, 120)
        self.setWindowTitle('Числовая игра')

        self.lcdX = QLCDNumber(self)
        self.lcdX.move(120, 10)
        self.lcdX.display(self.x)

        self.btnY = QPushButton(str(self.y), self)
        self.btnY.resize(40, 23)
        self.btnY.move(70, 10)

        self.btnZ = QPushButton(str(self.z), self)
        self.btnZ.resize(40, 23)
        self.btnZ.move(195, 10)

        self.labStep = QLabel(self)
        self.labStep.move(180, 45)
        self.labStep.setText('10')

        self.labhod = QLabel("Осталось ходов:", self)
        self.labhod.move(115,45)

        self.labRez = QLabel(self)
        self.labRez.move(130, 60)
        self.labRez.resize(50,20)
        self.labRez.setText("Result")

        self.btn_reset = QPushButton('New game', self)
        self.btn_reset.move(12, 10)
        self.btn_reset.resize(45, 23)

        self.btnY.clicked.connect(self.action)
        self.btnZ.clicked.connect(self.action)
        self.btn_reset.clicked.connect(self.action)


    def action(self):
        if self.sender() == self.btnY:
            self.x += self.y
            self.lcdX.display(self.x)
        if self.sender() == self.btnZ:
            self.x -= self.z
            self.lcdX.display(self.x)
        self.labStep.setText(str(int(self.labStep.text()) - 1))
        if self.x == 0:
            self.labRez.setText("Вы выиграли!")
        if self.x != 0 and int(self.labStep.text()) == 0:
            self.reset()
        if self.sender() == self.btn_reset:
            self.reset()


    def reset(self):
        self.x = random.randint(10, 30)
        self.y = random.randint(2, 10)
        self.z = random.randint(2, 10)
        self.labStep.setText('10')
        self.lcdX.display(self.x)
        self.btnY.setText(str(self.y))
        self.btnZ.setText(str(self.z))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())