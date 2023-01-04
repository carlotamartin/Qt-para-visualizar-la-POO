# Qt-para-visualizar-la-POO

Pasos de implementación:
1. Cree una ventana principal, agréguele una barra de estado para mostrar la puntuación y cree un objeto de clase de tablero y agréguelo como widget central
2. Cree una clase llamada tablero que herede el QFrame
3. Dentro de la clase de tablero cree un objeto de temporizador que llama al método de temporizador después de cierta cantidad de tiempo
4. Dentro del método de temporizador llama a otra acción del juego de la serpiente como movimiento, comida comida y si la serpiente se suicidó
5. Cree un método de evento de pulsación de tecla que verifique si las teclas de flecha están pulsado y cambiar la dirección de la serpiente de acuerdo con él.
6. Cree un método de evento de pintura que dibuje la serpiente y la comida
7. Cree un método de movimiento para mover la serpiente según la dirección
8. Cree un método de comida consumida que verifique la posición actual de la serpiente y la posición si se come comida, elimine la comida actual, aumente la longitud de la serpiente y suelte una nueva comida en una ubicación aleatoria.
9. Cree un método de verificación de suicidio que verifique si la posición de la cabeza de serpiente es similar a la posición del cuerpo o no, si las coincidencias detienen el temporizador y muestran el mensaje