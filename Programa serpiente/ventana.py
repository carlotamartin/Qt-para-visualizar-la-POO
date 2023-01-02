#Importamos las librerías necesarias
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget, QLabel, QHBoxLayout
import sys #Importamos sys para poder usar sys.exit, que nos permite cerrar la aplicación



class Ventana(QMainWindow): #Creamos la clase Ventana, que hereda de QMainWindow
    def __init__(self): #Definimos el método __init__
        super().__init__() #Llamamos al método __init__ de la clase padre
        self.setWindowTitle("Juego de la serpiente") #Establecemos el título de la ventana
        self.setFixedSize(800, 600) #Establecemos el tamaño de la ventana
        self.centrar() #Llamamos al método centrar
        self.initUI() #Llamamos al método initUI


    def initUI(self):
        #La barra de estado
        self.statusBar().showMessage('Puntuación: 0')

        #El botón de reinicio
        self.boton_reinicio = QPushButton("Reiniciar", self)
        self.boton_reinicio.move(700, 10)
        self.boton_reinicio.clicked.connect(self.reiniciar)

        #La etiqueta de puntuación
        self.etiqueta_puntuacion = QLabel("Puntuación: 0", self)
        self.etiqueta_puntuacion.move(10, 10)

        #La etiqueta de nivel
        self.etiqueta_nivel = QLabel("Nivel: 1", self)
        self.etiqueta_nivel.move(10, 30)

        #La etiqueta de vidas
        self.etiqueta_vidas = QLabel("Vidas: 3", self)
        self.etiqueta_vidas.move(10, 50)

    def reiniciar(self):
        self.statusBar().showMessage('Puntuación: 0')
        self.etiqueta_puntuacion.setText("Puntuación: 0")
        self.etiqueta_nivel.setText("Nivel: 1")
        self.etiqueta_vidas.setText("Vidas: 3")

    def centrar(self): #Definimos el método centrar
        frame = self.frameGeometry() #Obtenemos el marco de la ventana
        pantalla = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos()) #Obtenemos el número de pantalla en la que se encuentra el cursor
        centro = QApplication.desktop().screenGeometry(pantalla).center() #Obtenemos el centro de la pantalla en la que se encuentra el cursor
        frame.moveCenter(centro) #Movemos el marco al centro de la pantalla
        self.move(frame.topLeft()) #Movemos la ventana al punto superior izquierdo del marco



if __name__ == "__main__": #Si estamos ejecutando el script
    app = QApplication(sys.argv) #Creamos la aplicación
    ventana = Ventana() #Creamos una instancia de la clase Ventana
    ventana.show() #Mostramos la ventana
    sys.exit(app.exec_()) #Ejecutamos la aplicación y cerramos cuando se cierre la ventana
