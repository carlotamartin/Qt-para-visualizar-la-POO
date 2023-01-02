#Importamos las librerías necesarias
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPalette, QBrush, QPixmap #Importamos QPalette, QBrush y QPixmap para poder establecer el fondo de la ventana
import sys #Importamos sys para poder usar sys.exit, que nos permite cerrar la aplicación, y sys.argv, que nos permite pasar argumentos a la aplicación
from PyQt5.QtWidgets import QFrame


class Ventana(QMainWindow): #Creamos la clase Ventana, que hereda de QMainWindow

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("QWidget { background: #3a9b0f }")

        # Agrega la barra de estado aquí
        self.statusBar().showMessage('Puntuación: 0')

        # Crea un objeto de clase Board y establece como widget central
        board = Tablero()
        self.setCentralWidget(board)

        # Establece el título de la ventana
        self.setWindowTitle('El juego de la serpiente')


#Creamos la clase Tablero, que hereda de QWidget
class Tablero(QFrame):
    def __init__(self): #Definimos el método __init__
        super().__init__() #Llamamos al método __init__ de la clase padre
        self.initUI() #Llamamos al método initUI

    #Definimos el método initUI, que inicializa la interfaz de usuario
    def initUI(self):
        # Establece el tamaño del widget
        self.setFixedSize(548, 483)

        # Crea un layout horizontal y establece como layout del widget
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Crea un objeto QPalette y establece la imagen de fondo
        palette = QPalette()
        brush = QBrush(QPixmap('fondo.png'))
        palette.setBrush(QPalette.Background, brush)

        # Establece el objeto QPalette como el fondo del widget
        self.setPalette(palette)



if __name__ == "__main__": #Si estamos ejecutando el script
    app = QApplication(sys.argv) #Creamos la aplicación
    ventana = Ventana() #Creamos una instancia de la clase Ventana
    ventana.show() #Mostramos la ventana
    sys.exit(app.exec_()) #Ejecutamos la aplicación y cerramos cuando se cierre la ventana
