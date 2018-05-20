import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main_class.imageClassify import ImageClassify


class MainFrame(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.content_area()

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.content_box)

        self.setLayout(main_layout)

        self.show()


    def content_area(self):

        file_btn = QPushButton("file open")
        file_btn.clicked.connect(self.file_open_dialog)

        self.image_view = QLabel()

        self.root = "../images/test.jpg"
        self.pixmap = QPixmap(self.root)

        self.image_view.setPixmap(self.pixmap)
        self.image_view.setFixedWidth(self.width)
        self.image_view.setFixedHeight(450)

        image_text = "result"
        self.result = QLabel(image_text)


        self.content_box = QVBoxLayout()
        self.content_box.addWidget(file_btn)
        self.content_box.addWidget(self.image_view)
        self.content_box.addWidget(self.result)

    def file_open_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.root = fileName

        classify_image = ImageClassify()
        get_image_name = classify_image.image_processs(self.root)
        self.result.setText(get_image_name)


        self.pixmap = QPixmap(self.root)
        self.image_view.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainFrame()
    sys.exit(app.exec_())