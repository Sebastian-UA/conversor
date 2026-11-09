
# Importar herramientas de PySide6
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog


# Función para seleccionar un archivo
def seleccionar_archivo():

    archivo, _ = QFileDialog.getOpenFileName( #asi se usa la funcion
        ventana,
        "Seleccionar PowerPoint",
        "",
        "Archivos PowerPoint (*.pptx)"
    )

    if archivo:
        texto.setText(archivo)


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

# Crear un diseño vertical
layout = QVBoxLayout()

# Agregar el texto al diseño
layout.addWidget(texto)

# Agregar el botón al diseño
layout.addWidget(boton)

# Asignar el diseño a la ventana
ventana.setLayout(layout)

# Mostrar la ventana
ventana.show()

# Mantener la aplicación ejecutándose
app.exec()
