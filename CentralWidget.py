#Erstellen Sie ein CentralWidgets, welches fünf QLineEdits enthält. Zu jedem QLineEdit
#gehört ein QLabel mit der Beschriftung zur Eingabe:
#Zahlen im Dezimalsystem zwischen 0 und 9999.
#Sechstellige Hexadezimalwerte
#Binärzahlen, zwischen 2**2 und 2**10
#Nur Buchstaben (a-z, A-Z)
#Eingabe von Groß- und Kleinbuchstaben, welche in Großbuchstaben umgewandelt werden




from PyQt6.QtWidgets import QWidget, QSlider, QTextEdit, QTextBrowser, QGridLayout, QLabel, QPushButton, QLineEdit, \
    QApplication, QMessageBox


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.dezimalzahlen = QLabel("Zahlen im Dezimalsystem zwischen 0 und 9999", self)
        self.dezimalzahlen1 = QLineEdit(self)
        self.dezimalzahlen1.setInputMask("9000")

        self.hexadezimalwerte = QLabel("Sechstellige Hexadezimalwerte", self)
        self.hexadezimalwerte1 = QLineEdit(self)
        self.hexadezimalwerte1.setInputMask("hhhhhh")

        self.binaerzahlen = QLabel("Binärezahlen, zwischen 2**2 und 2**10", self)
        self.binaerzahlen1 = QLineEdit(self)
        self.dezimalzahlen1.setInputMask("BBBbbbbbb")

        self.buchstaben = QLabel("Nur Buchstaben(a-z, A-Z)", self)
        self.buchstaben1 = QLineEdit(self)

        self.kleinegroßebuchstaben = QLabel("Eingabe von Groß-und Kleinbuchstaben umgewandelt werden", self)
        self.kleinegroßebuchstaben1 = QLineEdit(self)

        layout= QGridLayout(self)

        layout.addWidget(self.dezimalzahlen, 1, 1)
        layout.addWidget(self.dezimalzahlen1, 2, 1)
        layout.addWidget(self.hexadezimalwerte, 3, 1)
        layout.addWidget(self.hexadezimalwerte1, 4, 1)
        layout.addWidget(self.binaerzahlen, 5, 1)
        layout.addWidget(self.binaerzahlen1, 6, 1)
        layout.addWidget(self.buchstaben, 7, 1)
        layout.addWidget(self.buchstaben1, 8, 1)
        layout.addWidget(self.kleinegroßebuchstaben, 9, 1)
        layout.addWidget(self.kleinegroßebuchstaben1, 10, 1)

    def einlogin(self):
        if self.dezimalzahlen.text() > 0 and self.dezimalzahlen1.text() < 9999:
            QMessageBox.information(self, "Titel", "Dezimalzahl")
        else:
            QMessageBox.information(self, "Titel", " kein Dezimalzahl#")