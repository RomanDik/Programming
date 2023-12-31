import sys

from part_1 import make_annotation
from part_2 import make_dataset_2, make_annotation_2
from part_3 import make_dataset_3, make_annotation_3
from part_5 import Iterator

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import  *


class Window(QMainWindow):
    
    def __init__(self) -> None:
        """Вызов методов"""
        super().__init__()
        self.initUI()
        self.initIterators()
        self.createActions()
        self.createMenuBar()
        self.setGeometry(450, 200, 1200, 800)

    
    def initUI(self) -> None:
        """Главноt окно и кнопки"""
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

    
    def initIterators(self) -> None:
        """Два объекта-итератора"""
        self.polarbear = Iterator('polarbear', 'dataset')
        self.brownbear = Iterator('brownbear', 'dataset')

    
    def nextpolarbear(self) -> None:
        """Следующий polarbear"""
        lbl_size = self.lbl.size()
        next_image = next(self.polarbear)
        if next_image != None:
            img = QPixmap(next_image).scaled(lbl_size, Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            self.initIterators()
            self.nextpolarbear()

    
    def nextbrownbear(self) -> None:
        """Следующий brownbear"""
        lbl_size = self.lbl.size()
        next_image = next(self.brownbear)
        if next_image != None:
            img = QPixmap(next_image).scaled(lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            self.initIterators()
            self.nextbrownbear()

   
    def createMenuBar(self) -> None:
        """Меню и действия"""
        menuBar = self.menuBar()

        self.fileMenu = menuBar.addMenu('&Menu')
        self.fileMenu.addAction(self.changeAction)

        self.annotationMenu = menuBar.addMenu('&Annotation')
        self.annotationMenu.addAction(self.createannotationAction)

        self.dataMenu = menuBar.addMenu('&Other Dataset')
        self.dataMenu.addAction(self.createData2Action)
        self.dataMenu.addAction(self.createData3Action)

    
    def createActions(self) -> None:
        """Действия в меню"""
        
        self.changeAction = QAction('&Change dataset')
        self.changeAction.triggered.connect(self.changeDataset)

        self.createannotationAction = QAction('&Create annotation')
        self.createannotationAction.triggered.connect(self.createAnnotation)

        self.createData2Action = QAction('&dataset2')
        self.createData2Action.triggered.connect(self.Dataset2)

        self.createData3Action = QAction('&dataset3')
        self.createData3Action.triggered.connect(self.Dataset3)
    
        
    
    def createAnnotation(self) -> None:
        """Аннотация для текущего dataset"""
        if 'dataset' in str(self.folderpath):
            make_annotation(self.folderpath)
        elif 'dataset_2' in str(self.folderpath):
            make_annotation_2(self.folderpath)
        elif 'dataset_3' in str(self.folderpath):
            make_annotation_3(self.folderpath)

    
    def changeDataset(self) -> None:
        """Действия с dataset...
        Изменение текущего dataset"""
        reply = QMessageBox.question(self, 'Warning', f'Are you sure you want to change current dataset?\nCurrent dataset: {str(self.folderpath)}', QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        else:
            pass
    
    
    def Dataset2(self) -> None:
        """Создание dataset_2 (имя класса и номер)"""
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        make_dataset_2(self.folderpath)
        

    
    def Dataset3(self) -> None:
        """Создание dataset_3 (рандом)"""
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        make_dataset_3(self.folderpath)

    
    def closeEvent(self, event: QEvent) -> None:
        """Подтверждение"""
        reply = QMessageBox.question(self, 'Message', 'Are you sure to escape?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main() -> None:
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()