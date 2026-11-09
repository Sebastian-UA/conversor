from docx import Document
from docx.shared import Pt, Cm

# Crear un documento Word
documento = Document()

# Configurar los márgenes de la hoja
seccion = documento.sections[0]

seccion.top_margin = Cm(1.5) #Define un margen de 1,5 centímetros.
seccion.bottom_margin = Cm(1.5)
seccion.left_margin = Cm(2)
seccion.right_margin = Cm(2)

# Configurar el estilo normal del documento
estilo = documento.styles["Normal"]

estilo.font.name = "Arial"
estilo.font.size = Pt(10)#Define el tamaño de letra en 10 puntos.

estilo.paragraph_format.space_before = Pt(0)#Espacio antes del párrafo.
estilo.paragraph_format.space_after = Pt(2)#Espacio después del párrafo.
estilo.paragraph_format.line_spacing = 1.0#Espaciado entre líneas.

# Agregar contenido de ejemplo
documento.add_heading("PRIMER", level=1)

documento.add_paragraph(
    "ESTE ES EL PRIMER PARRAFO DE LA PRIMERA DIAPO jeje"
)

documento.add_paragraph("Crear un conversor:")

documento.add_paragraph(
    "Leer archivos PowerPoint.",
    style="List Bullet"#Crea una viñeta.
)

documento.add_paragraph(
    "Generar documentos Word.",
    style="List Bullet"#Crea una viñeta.
)

documento.add_heading("SEGUNDO", level=1)

documento.add_paragraph("Segunda diapo jiji")

documento.add_heading("TERCERO", level=1)

documento.add_paragraph("EL FINAL de la diapo, wuaja")

# Guardar el documento
documento.save("resultado.docx")