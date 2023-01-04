#Importamos las librerías necesarias
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter #Importamos QPalette, QBrush y QPixmap para poder establecer el fondo de la ventana
import sys #Importamos sys para poder usar sys.exit, que nos permite cerrar la aplicación, y sys.argv, que nos permite pasar argumentos a la aplicación
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import * #Importamos QBasicTimer para poder usar un temporizador


class Ventana(QMainWindow): #Creamos la clase Ventana, que hereda de QMainWindow

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Agrega la barra de estado aquí
        self.statusBar().showMessage('Puntuación: 0')

        # Crea un objeto de clase Board y establece como widget central
        board = Tablero()
        self.setCentralWidget(board)

        # Establece el título de la ventana
        self.setWindowTitle('El juego de la serpiente')



#Creamos la clase Tablero, que hereda de QFrame, que es un widget que sirve para dibujar líneas y formas
class Tablero(QFrame):
    def __init__(self): #Definimos el método __init__
        super().__init__() #Llamamos al método __init__ de la clase padre
        self.initUI() #Llamamos al método initUI


    #Definimos el método initUI, que inicializa la interfaz de usuario
    def initUI(self):

        # Establece el tamaño del widget
        self.setFixedSize(548, 483)

        # Establece el color de fondo del widget
        self.setStyleSheet("QWidget { background: #3a9b0f }")

        # Crea un layout horizontal y establece como layout del widget
        layout = QHBoxLayout()
        self.setLayout(layout)

        # creating a timer
        self.timer = QBasicTimer()

        # Inicia el temporizador
        self.timer.start(100, self)


    #Creamos el método con el que se mueve la serpiente
    def movimiento(self):
        pass

    #Creamos el método con el que se comprueba si la serpiente se ha comido a sí misma
    def suicidio(self):
        pass

    #utilizaremos la clase QRandomGenerator para generar una nueva ubicación aleatoria para la comida y verificar
    # si la cabeza de la serpiente está en la misma posición que la comida. Si es así, puedes eliminar la comida actual,
    #  aumentar la longitud de la serpiente y soltar una nueva comida en una ubicación aleatoria.
    def comida(self):
        # Obtener la posición de la cabeza de la serpiente
        x, y = self.snake[0]

        # Si la cabeza de la serpiente está en la misma posición que la comida
        if x == self.food[0] and y == self.food[1]:

            # Elimina la comida actual
            self.food = None

            # Aumenta la longitud de la serpiente
            x, y = self.snake[-1]
            self.snake.append((x, y))

            # Llama al método para generar una nueva comida
            self.nueva_comida()


    #Creamos el método para generar una nueva comida
    def nueva_comida(self):
        # Genera una nueva ubicación aleatoria para la comida
        x = QRandomGenerator.global_().bounded(0, 548)
        y = QRandomGenerator.global_().bounded(0, 483)

        # Establece la nueva ubicación de la comida
        self.food = (x, y)

    #. Dentro del método de temporizador llama a otra acción del juego de la serpiente como movimiento, comida comida y si la serpiente se suicidó
    def tiempo (self, event):
        if event.timerId() == self.timer.timerId():

            # Llama a los métodos de movimiento, comida y suicidio
            self.movimiento()
            self.comida()
            self.suicidio()

            # Actualiza el tablero
            self.update()
        else:
            super().timerEvent(event)

    #Creamos el método para dibujar
    def dibujo(self, event):
        painter = QPainter(self)

        # Dibuja la serpiente
        for x, y in self.snake:
            painter.drawRect(x, y, 10, 10) #Cada vez que la serpiente se mueve, se dibuja un rectángulo en la posición actual de la cabeza

        # Dibuja la manzana
        x, y = self.food
        painter.drawEllipse(x, y, 10, 10)

    #Creamos el método para mover la serpiente
    def movimiento(self):

        #Para realizar este movimiento, vamos a suponer una pila, donde queremos añadir elementos por un lado y
        # eliminarlos por el otro. Para ello, vamos a usar el método insert, que añade un elemento en una posición determinada,
        #  y el método pop, que elimina el último elemento de la lista.


        # Obtener la cabeza de la serpiente
        x, y = self.snake[0]

        # Mover la cabeza de la serpiente en función de la dirección actual
        if self.snake_direction == "left":
            x -= 10
        elif self.snake_direction == "right":
            x += 10
        elif self.snake_direction == "up":
            y -= 10
        elif self.snake_direction == "down":
            y += 10

        # Actualizar la posición de la cabeza de la serpiente
        self.snake.insert(0, (x, y))

        # Eliminar el último segmento de la serpiente
        self.snake.pop()


    #Creamos el método para verificar si se ha pulsado una tecla de flecha
    def Pulsado(self, event):

        if event.key() == Qt.Key_Left:
            self.snake_direction = "left"
        elif event.key() == Qt.Key_Right:
            self.snake_direction = "right"
        elif event.key() == Qt.Key_Up:
            self.snake_direction = "up"
        elif event.key() == Qt.Key_Down:
            self.snake_direction = "down"




if __name__ == "__main__": #Si estamos ejecutando el script
    app = QApplication(sys.argv) #Creamos la aplicación
    ventana = Ventana() #Creamos una instancia de la clase Ventana
    ventana.show() #Mostramos la ventana
    sys.exit(app.exec_()) #Ejecutamos la aplicación y cerramos cuando se cierre la ventana
