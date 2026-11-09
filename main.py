
# Importar herramientas de PySide6
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog


# Variable para guardar la ruta del PowerPoint
ruta_powerpoint = ""

# Variable para guardar la ruta del documento Word
ruta_word = ""


# Función para seleccionar un archivo
def seleccionar_archivo():

    global ruta_powerpoint  # Necesitamos que la ruta seleccionada quede guardada y disponible para las demás funciones.

    ruta_powerpoint, _ = QFileDialog.getOpenFileName(
        ventana,
        "Seleccionar PowerPoint",
        "",
        "Archivos PowerPoint (*.pptx)"
    )

    if ruta_powerpoint:
        texto.setText(ruta_powerpoint)


# Función para seleccionar dónde guardar el Word
def seleccionar_destino():

    global ruta_word

    ruta_word, _ = QFileDialog.getSaveFileName(
        ventana,
        "Guardar documento Word",
        "",
        "Documentos Word (*.docx)"
    )

    if ruta_word:
        texto_destino.setText(ruta_word)


# Crear la aplicación
app = QApplication([])

# Crear una ventana
ventana = QWidget()

# Configurar la ventana
ventana.setWindowTitle("Conversor PowerPoint a Word")
ventana.resize(500, 300)

# Crear un texto
texto = QLabel("Ningún archivo seleccionado")

# Crear un botón
boton = QPushButton("Seleccionar PowerPoint")

# Conectar el botón con la función
boton.clicked.connect(seleccionar_archivo)


# Crear un texto para mostrar el destino
texto_destino = QLabel("Ningún destino seleccionado")

# Crear un botón para seleccionar el destino
boton_destino = QPushButton("Seleccionar destino Word")

# Conectar el botón con la función
boton_destino.clicked.connect(seleccionar_destino)


# Crear un diseño vertical
layout = QVBoxLayout()

# Agregar el texto al diseño
layout.addWidget(texto)

# Agregar el botón al diseño
layout.addWidget(boton)

# Agregar el texto y botón del destino
layout.addWidget(texto_destino)
layout.addWidget(boton_destino)


# Asignar el diseño a la ventana
ventana.setLayout(layout)

# Mostrar la ventana
ventana.show()

# Mantener la aplicación ejecutándose
app.exec()
