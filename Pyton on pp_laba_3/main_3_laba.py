import sys

from part_1 import make_annotation
from part_2 import make_dataset_2, make_annotation_2
from part_3 import make_dataset_3, make_annotation_3
from part_5 import Iterator

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import  *


class Window(QMainWindow):
    """Вызов методов"""
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initIterators()
        self.createActions()
        self.createMenuBar()
        self.setGeometry(450, 200, 1000, 700)

    """главноt окно и кнопоки"""
    def initUI(self) -> None:
        self.setWindowTitle('polarbear/brownbear')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        polarbear_btn = QPushButton('Next polarbear', self)
        brownbear_btn = QPushButton('Next brownbear', self)

        self.lbl = QLabel(self)
        self.lbl.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(polarbear_btn)
        hbox.addWidget(brownbear_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)

        self.centralWidget.setLayout(vbox)

        polarbear_btn.clicked.connect(self.nextpolarbear)
        brownbear_btn.clicked.connect(self.nextbrownbear)

        self.folderpath = ' '

        self.show()

def main() -> None:
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()