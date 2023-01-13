# Juego de la Serpiente con PyQt5

Este es un juego clásico de la serpiente desarrollado con PyQt5 en Python.

### Requisitos
 - Python 3.x
 - PyQt5

 ### Instalación
Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu terminal:

`pip install pyqt5`

### Ejecución
Para ejecutar el juego, simplemente abre una terminal en la carpeta `\Porgrama serpiente` donde se encuentra el archivo ventana.py y ejecuta el siguiente comando:

`python snake_game.py`

### Jugando
Al ejecutar el juego, se abrirá una ventana con un botón para inciar el juego. Utiliza las flechas del teclado para mover la serpiente e intentar comer las máximas manzanas posibles. Pierdes cuando la serpeinte choca con si misma.


### Pasos de ejecucción
Los pasos que he realizado para hacer le programa:
1. Cree una ventana principal, agréguele una barra de estado para mostrar la puntuación y cree un objeto de clase de tablero y agréguelo como widget central
2. Cree una clase llamada tablero que herede el QFrame
3. Dentro de la clase de tablero cree un objeto de temporizador que llama al método de temporizador después de cierta cantidad de tiempo
4. Dentro del método de temporizador llama a otra acción del juego de la serpiente como movimiento, comida comida y si la serpiente se suicidó
5. Cree un método de evento de pulsación de tecla que verifique si las teclas de flecha están pulsado y cambiar la dirección de la serpiente de acuerdo con él.
6. Cree un método de evento de pintura que dibuje la serpiente y la comida
7. Cree un método de movimiento para mover la serpiente según la dirección
8. Cree un método de comida consumida que verifique la posición actual de la serpiente y la posición si se come comida, elimine la comida actual, aumente la longitud de la serpiente y suelte una nueva comida en una ubicación aleatoria.
9. Cree un método de verificación de suicidio que verifique si la posición de la cabeza de serpiente es similar a la posición del cuerpo o no, si las coincidencias detienen el temporizador y muestran el mensaje
