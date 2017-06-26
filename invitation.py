from docx import Document
from docx.shared import Inches, Pt
from dates import dates

def speaker (name, org):
    document = Document('./format/invitation.docx')
    style = document.styles['Title']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(12)
    font.bold = True
    ds = dates()

    for paragraph in document.paragraphs:
        if 'Nombre' in paragraph.text:
            paragraph.style = document.styles['Title']
            paragraph.text = name
        elif 'Organización' in paragraph.text:
            paragraph.style = document.styles['Title']
            paragraph.text = org
        elif 'Fecha1' in paragraph.text:
            paragraph.text = ds[0]
        elif 'Fecha2' in paragraph.text:
            paragraph.text = ds[1]
        elif 'Fecha3' in paragraph.text:
            paragraph.text = ds[2]
        elif 'Fecha4' in paragraph.text:
            paragraph.text = ds[3]

    document.save('./invitation/invitacion_ponencia.docx')
