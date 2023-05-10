from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text  import WD_PARAGRAPH_ALIGNMENT
from docx.image.image import *
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.shape import WD_INLINE_SHAPE
from docx2pdf import convert
from docx.shared import RGBColor


document = Document('existing_template.docx')




##Code here to handle patient data and selected graphs, add to functions
def get_graph_data(document, name, address, age, contact, graph_selected):
    print (name, address, age, contact, graph_selected)
    
    p = document.add_paragraph('Name: ' + name + ' \n Age: '+ age +
                               '\n Address: ' + address + '\n Contact Num: '+ contact)
    first_run = p.runs[0]
    font = first_run.font
    font.color.rgb = RGBColor(255, 255, 255)  # white color
    font.size = Pt(16)
    p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    p.space_before = Inches(3)
    p.right_indent = Inches(7) - (p.paragraph_format.left_indent or Inches(0)) - (p.paragraph_format.first_line_indent or Inches(0)) - (p.paragraph_format.space_before or Pt(0))

    

    # add the image to the document
    image_path = 'Knee_Flexion.png'

    # set the position and size of the image
    width = Inches(4)
    height = Inches(3)
    image = document.add_picture(image_path)
    left = Inches(2)
    top = Inches(4)
    image.left = left
    image.top = top
    image.width = width
    image.height = height


    # add the image to the document
    image_path = 'Elbow_Flexion.png'
    image = document.add_picture(image_path)

    # get the image dimensions
    image_width = image.width
    image_height = image.height

    # set the position of the image in the page (in EMU)
    left = Inches(2)
    top = Inches(4)

    # set the image size
    width = Inches(4)
    height = Inches(3)

    # set the position and size of the image
    image.left = left
    image.top = top
    image.width = width
    image.height = height

    p = document.add_paragraph("wdwdqdwdqw")

    # add the image to the document
    image_path = 'Pelvis_Flexion.png'
    image = document.add_picture(image_path)

    # get the image dimensions
    image_width = image.width
    image_height = image.height

    # set the position of the image in the page (in EMU)
    left = Inches(2)
    top = Inches(4)

    # set the image size
    width = Inches(4)
    height = Inches(3)

    # set the position and size of the image
    image.left = left
    image.top = top
    image.width = width
    image.height = height

    # save the document
    document.save('Modified.docx')


    input_file = "Modified.docx"
    output = "report.pdf"

    convert(input_file, output)



get_graph_data(document, name="name", address="fhk3qw", age="12", contact="293742", graph_selected="jda" )