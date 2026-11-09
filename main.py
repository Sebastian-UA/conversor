# Importar herramientas de PySide6
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QMessageBox ,QGroupBox
from conversor import convertir
from PySide6.QtCore import Qt

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

    # Activar el botón solamente si ambas rutas están seleccionadas
    boton_convertir.setEnabled(bool(ruta_powerpoint and ruta_word))


# Función para seleccionar dónde guardar el Word
def seleccionar_destino():

    global ruta_word

    ruta_word, _ = QFileDialog.getSaveFileName(
        ventana,
        "Guardar documento Word",
        "documento_convertido.docx",  # nombre que le damos al archivo
        "Documentos Word (*.docx)"
    )

    if ruta_word and not ruta_word.lower().endswith(".docx"):
        ruta_word += ".docx"

    if ruta_word:
        texto_destino.setText(ruta_word)

    # Activar el botón solamente si ambas rutas están seleccionadas
    boton_convertir.setEnabled(bool(ruta_powerpoint and ruta_word))


# Función para convertir el PowerPoint a Word
def convertir_archivo():

    if not ruta_powerpoint:
        QMessageBox.critical(
            ventana,
            "Error",
            "Primero debes seleccionar un PowerPoint"
        )
        return

    if not ruta_word:
        QMessageBox.critical(
            ventana,
            "Error",
            "Primero debes seleccionar un lugar donde guardar el archivo"
        )
        return

    resultado = convertir(ruta_powerpoint, ruta_word)

    if resultado:
        QMessageBox.information(
            ventana,
            "Éxito",
            "Documento creado correctamente"
        )

    else:
        QMessageBox.critical(
            ventana,
            "Error",
            "No se pudo crear el documento"
        )


# CREAR LA APLICACION
app = QApplication([])

# Crear una ventana
ventana = QWidget()

# Configurar la ventana
ventana.setWindowTitle("Conversor PowerPoint a Word")
ventana.resize(500, 300)
ventana.setStyleSheet("""
    QWidget {
        background-color: #f4f6f9;
        font-family: Arial;
    }
""")

# Crear el título de la aplicación
titulo = QLabel("Conversor PowerPoint a Word")
titulo.setStyleSheet("""
    font-size: 20px;
    font-weight: bold;
    color: #1e293b;
""")
titulo.setAlignment(Qt.AlignCenter)  # centrar titulo

# Crear una descripción
descripcion = QLabel("Selecciona una presentación y conviértela en un documento Word.")
descripcion.setStyleSheet("""
    font-size: 12px;
    color: #64748b;
""")
descripcion.setAlignment(Qt.AlignCenter)  # centrar descripcion

# Crear un texto
texto = QLabel("Ningún archivo seleccionado")

# Crear un botón
boton = QPushButton("Seleccionar PowerPoint")

# Conectar el botón con la función
boton.clicked.connect(seleccionar_archivo)

# Crear un botón para convertir
boton_convertir = QPushButton("Convertir")

# Desactivar el botón inicialmente
boton_convertir.setEnabled(False)

# Conectar el botón con la función
boton_convertir.clicked.connect(convertir_archivo)


# Crear un texto para mostrar el destino
texto_destino = QLabel("Ningún destino seleccionado")

# Crear un botón para seleccionar el destino
boton_destino = QPushButton("Seleccionar destino Word")

# Conectar el botón con la función
boton_destino.clicked.connect(seleccionar_destino)

# Crear sección para seleccionar PowerPoint
grupo_powerpoint = QGroupBox("Archivo de entrada")

# Crear diseño para la sección PowerPoint
layout_powerpoint = QVBoxLayout()

layout_powerpoint.addWidget(texto)
layout_powerpoint.addWidget(boton)

# Asignar diseño al grupo PowerPoint
grupo_powerpoint.setLayout(layout_powerpoint)

# Crear sección para seleccionar destino Word
grupo_word = QGroupBox("Archivo de salida")

# Crear diseño para la sección Word
layout_word = QVBoxLayout()

layout_word.addWidget(texto_destino)
layout_word.addWidget(boton_destino)

# Asignar diseño al grupo Word
grupo_word.setLayout(layout_word)


# Crear un diseño vertical
layout = QVBoxLayout()

# Configurar los espacios del diseño
layout.setSpacing(15)
layout.setContentsMargins(25, 25, 25, 25)

# titulo y descripcion
layout.addWidget(titulo)
layout.addWidget(descripcion)

# Agregar las secciones al diseño principal
layout.addWidget(grupo_powerpoint)
layout.addWidget(grupo_word)

# Agregar el botón de conversión
layout.addWidget(boton_convertir)

boton_convertir.setStyleSheet("""
    QPushButton {
        background-color: #2563eb;
        color: white;
        font-size: 14px;
        font-weight: bold;
        padding: 10px;
        border-radius: 6px;
    }
""")

# Asignar el diseño a la ventana
ventana.setLayout(layout)

# Mostrar la ventana
ventana.show()

# Mantener la aplicación ejecutándose
app.exec()