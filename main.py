
from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER
from pptx.oxml.ns import qn

# Nuevas importaciones para crear documentos Word
from docx import Document
from docx.shared import Pt, Cm


# Abrir una presentación PowerPoint
presentacion = Presentation("ejemplo.pptx")

# Crear un documento Word
documento = Document()


# Configurar los márgenes de la hoja Word
seccion = documento.sections[0]

seccion.top_margin = Cm(1.5)
seccion.bottom_margin = Cm(1.5)
seccion.left_margin = Cm(2)
seccion.right_margin = Cm(2)

# Configurar el estilo normal del documento
estilo = documento.styles["Normal"]

estilo.font.name = "Arial"
estilo.font.size = Pt(10)

estilo.paragraph_format.space_before = Pt(0)
estilo.paragraph_format.space_after = Pt(2)
estilo.paragraph_format.line_spacing = 1.0

# Configurar el estilo de los títulos
estilo_titulo = documento.styles["Heading 1"]

estilo_titulo.font.name = "Arial"
estilo_titulo.font.size = Pt(14)
estilo_titulo.font.bold = True

estilo_titulo.paragraph_format.space_before = Pt(5)
estilo_titulo.paragraph_format.space_after = Pt(2)


# Recorrer las diapositivas
for diapositiva in presentacion.slides:  # Permite acceder a todas las diapositivas

    for forma in diapositiva.shapes:  # Recorrer los elementos de cada diapositiva

        # Comprobar si el elemento contiene texto
        if not forma.has_text_frame:
            continue

        # Comprobar si el elemento es un placeholder
        if forma.is_placeholder:

            # Obtener el tipo de placeholder
            tipo = forma.placeholder_format.type

            # Identificar títulos
            if tipo == PP_PLACEHOLDER.TITLE or tipo == PP_PLACEHOLDER.CENTER_TITLE:
                nombre = "TÍTULO"

            # Identificar subtítulos
            elif tipo == PP_PLACEHOLDER.SUBTITLE:
                nombre = "SUBTÍTULO"

            # Otros tipos de contenido
            else:
                nombre = "CONTENIDO"

        else:
            nombre = "CONTENIDO"

        # Recorrer los párrafos de cada elemento
        for parrafo in forma.text_frame.paragraphs:

            # Evitar párrafos vacíos
            texto = parrafo.text.strip()

            if not texto:
                continue

            # Mostrar el nivel del párrafo
            print(f"Nivel: {parrafo.level}")

            # Obtener las propiedades XML del párrafo
            propiedades = parrafo._p.find(qn("a:pPr"))

            # Comprobar si tiene viñeta o numeración
            tiene_vineta = False
            tiene_numeracion = False

            if propiedades is not None:

                if propiedades.find(qn("a:buChar")) is not None:
                    tiene_vineta = True

                elif propiedades.find(qn("a:buAutoNum")) is not None:
                    tiene_numeracion = True

            # Mostrar el tipo de contenido
            if tiene_vineta:

                print(f"VIÑETA: {texto}")

                # Seleccionar el estilo según el nivel
                nivel_lista = parrafo.level + 1

                if nivel_lista == 1:
                    estilo_lista = "List Bullet"
                else:
                    estilo_lista = f"List Bullet {nivel_lista}"

                # Agregar la viñeta al documento Word
                parrafo_word = documento.add_paragraph(
                    texto,
                    style=estilo_lista
                )

            elif tiene_numeracion:

                print(f"NUMERACIÓN: {texto}")

                # Seleccionar el estilo según el nivel
                nivel_lista = parrafo.level + 1

                if nivel_lista == 1:
                    estilo_lista = "List Number"
                else:
                    estilo_lista = f"List Number {nivel_lista}"

                # Agregar el elemento numerado al documento Word
                parrafo_word = documento.add_paragraph( 
                    texto,
                    style=estilo_lista
                )

            elif nombre == "TÍTULO": 

                print(f"{nombre}: {texto}")

                parrafo_word = documento.add_heading(texto, level=1)

            elif nombre == "SUBTÍTULO":

                print(f"{nombre}: {texto}")

                parrafo_word = documento.add_paragraph()
                texto_word = parrafo_word.add_run(texto)

                texto_word.bold = True
                texto_word.font.size = Pt(11)

            else:

                print(f"{nombre}: {texto}")

                parrafo_word = documento.add_paragraph(texto)

                # Aplicar sangría según el nivel de PowerPoint
                parrafo_word.paragraph_format.left_indent = Cm(
                    0.5 * parrafo.level
                )

            # Configurar el espacio entre párrafos
            parrafo_word.paragraph_format.space_before = Pt(0)
            parrafo_word.paragraph_format.space_after = Pt(2)
            parrafo_word.paragraph_format.line_spacing = 1.0


# Guardar el documento Word
documento.save("resultado.docx")

print("¡Documento Word creado correctamente!")
