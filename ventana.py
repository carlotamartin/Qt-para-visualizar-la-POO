from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
import sys


class Snake_program(QMainWindow):
    def __init__(self):
        super(Snake_program, self).__init__()
        self.board = Tablero(self)

        #Creamos la barra superior
        self.statusbar = self.statusBar()
        self.board.msg2statusbar[str].connect(self.statusbar.showMessage)

        self.setCentralWidget(self.board)
        self.setWindowTitle('El juego de la serpiente')
        self.resize(600, 400)

        #Obtenemos la resolución de la pantalla
        screen = QDesktopWidget().screenGeometry()

        #Obtenemos el tamaño de la ventana
        tamaño = self.geometry()

        #Centramos la ventana
        self.move((screen.width()-tamaño.width())/2, (screen.height()-tamaño.height())/2)

        #Empieza el juego
        self.board.start()
        self.show()


class Tablero(QFrame):

    #Creamos una señal que nos permitirá enviar mensajes a la barra de estado
    msg2statusbar = pyqtSignal(str)
    #Creamos las variables velocidad, anchura y altura
    VELOCIDAD = 150
    pix_ancho = 60
    pix_largo = 40

    def __init__(self, parent):
        #LLamamos al constructor de la clase padre
        super(Tablero, self).__init__(parent)

        #Creamos el timer
        self.timer = QBasicTimer()

        #Creamos la serpiente, la cual es una lista de coordenadas donde cada coordenada va a ser un bocle. 
        #La cabeza de la serpiente es la primera coordenada de la lista
        #La cola de la serpiente es la última coordenada de la lista
        #Podemos interpretar la serpiente como una pila, donde vamos a tener la cabeza y la cola, y vamos a ir añadiendo
        #elementos a la pila cada vez que coma una manzana.
        self.snake = [[5, 10], [5, 11]]

        #Creamos la cabeza de la serpiente
        self.x_cabeza = self.snake[0][0]
        self.y_cabeza = self.snake[0][1]

        #Creamos la manzana
        self.apple = []

        #Creamos la variable que nos permitirá saber si la serpiente ha crecido o no
        self.crece_snake = False
        self.board = []

        #Creamos la variable que nos permitirá saber la dirección de la serpiente. Inicialmente la serpiente irá hacia la derecha
        self.direccion = 1

        #Tiramos la primera manzana
        self.tirar_apple()
        self.setFocusPolicy(Qt.StrongFocus)


    def square_width(self):
        return self.contentsRect().width() / Tablero.pix_ancho

    def square_height(self):
        return self.contentsRect().height() / Tablero.pix_largo

    def start(self):
        self.msg2statusbar.emit(str(len(self.snake) - 2))
        self.timer.start(Tablero.VELOCIDAD, self)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()
        boardtop = rect.bottom() - Tablero.pix_largo * self.square_height()

        for pos in self.snake:
            self.draw_square(painter, rect.left() + pos[0] * self.square_width(),
                             boardtop + pos[1] * self.square_height(),0x38761D )
        for pos in self.apple:
            self.draw_square(painter, rect.left() + pos[0] * self.square_width(),
                             boardtop + pos[1] * self.square_height(),0xFF0000 )

    def draw_square(self, painter, x, y, color):
        color = QColor(color)
        painter.fillRect(x + 1, y + 1, self.square_width() - 2, self.square_height() - 2, color)


    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            if self.direccion != 2:
                self.direccion = 1
        elif key == Qt.Key_Right:
            if self.direccion != 1:
                self.direccion = 2
        elif key == Qt.Key_Down:
            if self.direccion != 4:
                self.direccion = 3
        elif key == Qt.Key_Up:
            if self.direccion != 3:
                self.direccion = 4

    def move_snake(self):
        if self.direccion == 1:
            self.x_cabeza, self.y_cabeza = self.x_cabeza - 1, self.y_cabeza
            if self.x_cabeza < 0:
                self.x_cabeza = Tablero.pix_ancho - 1
        if self.direccion == 2:
            self.x_cabeza, self.y_cabeza = self.x_cabeza + 1, self.y_cabeza
            if self.x_cabeza == Tablero.pix_ancho:
                self.x_cabeza = 0
        if self.direccion == 3:
            self.x_cabeza, self.y_cabeza = self.x_cabeza, self.y_cabeza + 1
            if self.y_cabeza == Tablero.pix_largo:
                self.y_cabeza = 0
        if self.direccion == 4:
            self.x_cabeza, self.y_cabeza = self.x_cabeza, self.y_cabeza - 1
            if self.y_cabeza < 0:
                self.y_cabeza = Tablero.pix_largo

        head = [self.x_cabeza, self.y_cabeza]
        self.snake.insert(0, head)
        if not self.crece_snake:
            self.snake.pop()
        else:
            self.msg2statusbar.emit(str(len(self.snake)-2))
            self.crece_snake = False

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.move_snake()
            self.is_apple_collision()
            self.is_suicide()
            self.update()

    def is_suicide(self):  # If snake collides with itself, game is over
        for i in range(1, len(self.snake)):
            if self.snake[i] == self.snake[0]:
                self.msg2statusbar.emit(str("TRUP"))
                self.snake = [[x, y] for x in range(0, 61) for y in range(0, 41)]
                self.timer.stop()
                self.update()

    def is_apple_collision(self):
        for pos in self.apple:
            if pos == self.snake[0]:
                self.apple.remove(pos)
                self.tirar_apple()
                self.crece_snake = True

    def tirar_apple(self):
        x = random.randint(3, 58)
        y = random.randint(3, 38)
        for pos in self.snake:
            if pos == [x, y]:
                self.tirar_apple()
        self.apple.append([x, y])


def main():
    app = QApplication([])
    launch_game = Snake_program()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()